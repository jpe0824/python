import MemoGenSeqDC as dc
import GenSeqDP as dp
import random
import time
import pandas as pd

genetic_alphabet = ['A', 'C', 'G', 'T']

def generate_seq(n):
    return ''.join(random.choices(genetic_alphabet, k=n))

def est_dc_time_complexity(m,n):
    return 3 * (m * n) + 1

def main():
    # define the range of values for m and n
    m_values = [2**i for i in range(1, 7)]
    n_values = [2**i for i in range(1, 7)]

    # create an empty DataFrame to store the results
    results_df = pd.DataFrame(columns=["m", "n", "DP_time", "DP_ops", "memo_time", "memo_ops", "non_memo_time", "non_memo_ops"])

    print('loading...')
    # loop over the values of m and n and run the algorithms
    for m in m_values:
        for n in n_values:
            # generate two random sequences of length m and n
            s1 = generate_seq(m)
            s2 = generate_seq(n)

            # run the DP algorithm and measure the time and number of basic operations
            dp.reset()
            est_dp_time = dp.timeComplexity(m,n)
            start_time = time.time()
            DP_result = dp.geneSeqDP(s1, s2)
            DP_time = time.time() - start_time
            DP_ops = dp.basicOps()

            # run the memoized algorithm and measure the time and number of recursive calls
            dc.reset()
            est_dc_time = est_dc_time_complexity(m, n)
            dc.setS1(s1)
            dc.setS2(s2)
            start_time = time.time()
            memo_result = dc.memoGenSeqDC(len(s1)-1, len(s2)-1)
            memo_time = time.time() - start_time
            memo_ops = dc.basicOps()

            if((m * n) <= (2**7)):
                dc.reset()
                dc.setS1(s1)
                dc.setS2(s2)
                start_time = time.time()
                non_memo_result = dc.genSeqDC(len(s1)-1, len(s2)-1)
                non_memo_time = time.time() - start_time
                non_memo_ops = dc.basicOps()
            else:
                non_memo_result = '-'
                non_memo_time = '-'
                non_memo_ops = '-'

            # add the results to the DataFrame
            results_df = results_df._append({
                "m": m,
                "n": n,
                "est_DP_time_complexity": est_dp_time * (DP_time / DP_ops),
                "DP_time": DP_time,
                "DP_ops": DP_ops,
                "DP_time_per_op": DP_time / DP_ops,
                "est_DC_time_complexity": est_dc_time * (memo_time/memo_ops),
                "DC_time_per_op": memo_time/ memo_ops,
                "memo_time": memo_time,
                "memo_ops": memo_ops,
                "non_memo_time": non_memo_time,
                "non_memo_ops": non_memo_ops
            }, ignore_index=True)
            print(f'Results for m={m}, n={n}, s1={s1}, s2={s2}\n  DP_result: {DP_result}\n  memo_result: {memo_result}\n  non_memo_result: {non_memo_result}\n')
    # save the results to a CSV file
    results_df.to_csv("./results.csv", index=False)

if __name__ == '__main__':
    main()
