-- 1. Partition One of the Tables

-- -before explain
-- "Seq Scan on users  (cost=0.00..12.90 rows=290 width=248)"

-- -after explain
-- "Append  (cost=0.00..43.05 rows=870 width=248)"
-- "  ->  Seq Scan on new_users_100_104 new_users_1  (cost=0.00..12.90 rows=290 width=248)"
-- "  ->  Seq Scan on new_users_105_109 new_users_2  (cost=0.00..12.90 rows=290 width=248)"
-- "  ->  Seq Scan on new_users_110_plus new_users_3  (cost=0.00..12.90 rows=290 width=248)"


CREATE TABLE new_users (
   userid INTEGER,
   username VARCHAR(50) NOT NULL,
   password VARCHAR(50) NOT NULL,
   weight INTEGER,
   height INTEGER,
   PRIMARY KEY (userid)
) PARTITION BY RANGE (userid);

CREATE TABLE new_users_100_104 PARTITION OF new_users
   FOR VALUES FROM (100) TO (104);

CREATE TABLE new_users_105_109 PARTITION OF new_users
   FOR VALUES FROM (105) TO (109);

CREATE TABLE new_users_110_plus PARTITION OF new_users
   FOR VALUES FROM (110) TO (MAXVALUE);

--2. Stored procedure

CREATE OR REPLACE FUNCTION get_users_by_weight(_weight INTEGER)
RETURNS TABLE (userid INTEGER, username VARCHAR(50), weight INTEGER, height INTEGER) AS
$$
BEGIN
  RETURN QUERY SELECT users.userid, users.username, users.weight, users.height FROM users WHERE users.weight = _weight;
END;
$$
LANGUAGE plpgsql;

SELECT * FROM get_users_by_weight(145);

-- 3. Database Views and User Access to Views

CREATE VIEW users_view AS SELECT * FROM users;
CREATE VIEW workout_view AS SELECT * FROM workout;
CREATE VIEW workouttypes_view AS SELECT * FROM workouttypes;

CREATE ROLE ViewAll;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO ViewAll;

CREATE USER "admin" WITH PASSWORD 'password';
GRANT ViewAll TO admin;
--4. Create an Application Admin Role
CREATE ROLE AppAdmin;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO AppAdmin;

CREATE USER app_admin_user WITH PASSWORD 'your_password_here';
GRANT AppAdmin TO app_admin_user;

--5. Alter tables
ALTER TABLE users
ADD COLUMN age INTEGER;

ALTER TABLE workout
RENAME TO exercise;

--6. PK FK
-- already had these in my table but here are commands I would use

-- Create Primary Key constraints
ALTER TABLE users ADD CONSTRAINT users_pk PRIMARY KEY (userid);
ALTER TABLE workout ADD CONSTRAINT workout_pk PRIMARY KEY (workoutid);
ALTER TABLE workouttypes ADD CONSTRAINT workouttypes_pk PRIMARY KEY (workouttypeid);

-- Create Foreign Key constraints
ALTER TABLE workout ADD CONSTRAINT workout_userid_fk FOREIGN KEY (userid) REFERENCES users(userid);
ALTER TABLE workout ADD CONSTRAINT workout_workouttypeid_fk FOREIGN KEY (workouttypeid) REFERENCES workouttypes(workouttypeid);

--7. Table Auditing using Triggers

CREATE TABLE users_history (
  id SERIAL PRIMARY KEY,
  user_id INTEGER NOT NULL,
  username VARCHAR(50) NOT NULL,
  password VARCHAR(50) NOT NULL,
  weight INTEGER NOT NULL,
  height INTEGER NOT NULL,
  changed_by VARCHAR(50) NOT NULL,
  change_time TIMESTAMP NOT NULL DEFAULT NOW(),
  is_new BOOLEAN NOT NULL
);

CREATE OR REPLACE FUNCTION users_history_trigger()
RETURNS TRIGGER AS $$
BEGIN
  IF TG_OP = 'UPDATE' THEN
    INSERT INTO users_history (user_id, username, password, weight, height, changed_by, is_new)
    VALUES (OLD.userid, OLD.username, OLD.password, OLD.weight, OLD.height, CURRENT_USER, false),
           (NEW.userid, NEW.username, NEW.password, NEW.weight, NEW.height, CURRENT_USER, true);
  ELSIF TG_OP = 'INSERT' THEN
    INSERT INTO users_history (user_id, username, password, weight, height, changed_by, is_new)
    VALUES (NEW.userid, NEW.username, NEW.password, NEW.weight, NEW.height, CURRENT_USER, true);
  END IF;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER users_history
AFTER INSERT OR UPDATE ON users
FOR EACH ROW
EXECUTE FUNCTION users_history_trigger();

-- 8. Check Constraints
ALTER TABLE users ADD CONSTRAINT check_weight_height CHECK (weight > 0 AND height > 0);

-- 9. Schema Creation and User Access

-- create the schema
CREATE SCHEMA my_schema;

-- create a copy of the users table in the new schema
CREATE TABLE my_schema.users AS
SELECT * FROM public.users;

-- grant permissions to a user for the new table
CREATE USER my_user WITH PASSWORD 'password';
GRANT SELECT, REFERENCES, UPDATE, DELETE ON TABLE my_schema.users TO my_user;

-- Application Report

CREATE VIEW workout_summary AS
SELECT users.username,
       exercise.date,
       workouttypes.workouttype,
       SUM(exercise.duration) as total_duration,
       SUM(exercise.calories) as total_calories
FROM users
INNER JOIN exercise ON users.userid = exercise.userid
INNER JOIN workouttypes ON exercise.workouttypeid = workouttypes.workouttypeid
GROUP BY users.username, exercise.date, workouttypes.workouttype;
