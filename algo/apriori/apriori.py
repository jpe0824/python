from typing import List

def apriori_gen(Itemset: List[str], itemset_length: int) -> List[str]:
    candidates = []
    for i in range(0, itemset_length):
        element = str(Itemset[i])
        for j in range(i + 1, itemset_length):
            element1 = str(Itemset[j])
            if element[0:(len(element) - 1)] == element1[0:(len(element1) - 1)]:
                unionset = element[0:(len(element) - 1)] + element1[len(element1) - 1] + element[len(element) - 1]
                unionset = ''.join(sorted(unionset))
                candidates.append(unionset)
    return candidates

def prune(Ck: dict, min_support: int) -> List[str]:
    frequent_itemsets = sorted([i for i in Ck if Ck[i] >= min_support])
    return frequent_itemsets

def count_subset(candidates: List[str], candidate_length: int) -> dict:
    Lk = dict()
    with open('example.txt') as file:
        for line in file:
            count = 0
            for i in range(0, candidate_length):
                key = str(candidates[i])
                if key not in Lk:
                    Lk[key] = 0
                flag = True
                for k in key:
                    if k not in line:
                        flag = False
                if flag:
                    Lk[key] += 1
    return Lk

def main():
    min_support = 3
    C1 = {}
    with open('example.txt') as file:
        for line in file:
            for item in line.split():
                if item in C1:
                    C1[item] += 1
                else:
                    C1[item] = 1
    frequent_itemsets = prune(C1, min_support)
    print(f'Frequent 1-itemset is {frequent_itemsets}')
    k = 2
    while frequent_itemsets:
        C = count_subset(frequent_itemsets, len(frequent_itemsets))
        frequent_itemsets = prune(C, min_support)
        print(f'Frequent {k}-itemset is {frequent_itemsets}')
        frequent_itemsets = apriori_gen(frequent_itemsets, len(frequent_itemsets))
        k += 1

if __name__ == '__main__':
    main()
