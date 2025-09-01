from itertools import chain, combinations, product
from typing import List, Tuple

LIST = [3, 4, 5, 15]
N = 20

patchCandidates = []


def makePermutation(subNums: List[int]) -> List[Tuple[int]]:
    # Generate powerset of subNums
    powerSet = list(chain.from_iterable(combinations(subNums, r) for r in range(len(subNums) + 1)))

    return powerSet


def getDiffs(permutations: List[Tuple[int]], k: int) -> set:
    diffs = set()
    for perm in permutations:
        diff = k - sum(perm)
        if diff >= 0:
            diffs.add(diff)

    return diffs


def getSublist(nums: List[int], k: int) -> List[int]:
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] < k:
            start = mid + 1
        else:
            end = mid - 1
    return nums[:start]


def findPresent(nums: List[int], n: int) -> bool:
    return n in nums


def addPatchCandidates(nums: List[int], k: int):
    if findPresent(nums, k):
        return

    sublist = getSublist(nums, k)
    permutations = makePermutation(sublist)
    diffs = getDiffs(permutations, k)
    if 0 in diffs:
        return
    patchCandidates.append(diffs)
    return


def findCommon() -> List[Tuple[int, ...]]:
    cleanSubsets()
    answers = makeSumSets()

    modified_answers = set(answers)
    to_remove = set()
    to_add = set()

    for answer in answers:
        for i in reversed(range(len(answer))):
            permutations = makePermutation(list(answer)[:i])
            diffs = getDiffs(permutations, list(answer)[i])
            if 0 in diffs:
                new_answer = list(answer)
                new_answer.pop(i)
                to_remove.add(answer)
                to_add.add(tuple(sorted(new_answer)))

    modified_answers.difference_update(to_remove)
    modified_answers.update(to_add)

    # Find the shortest length among the answers
    min_length = min(len(answer) for answer in modified_answers)

    # Filter the answers to return only those with the shortest length
    shortest_answers = [answer for answer in modified_answers if len(answer) == min_length]

    return shortest_answers


def cleanSubsets():
    to_remove = set()

    for i in range(len(patchCandidates)):
        for j in range(i + 1, len(patchCandidates)):
            if patchCandidates[i].issubset(patchCandidates[j]):
                to_remove.add(j)
            elif patchCandidates[i].issuperset(patchCandidates[j]):
                to_remove.add(i)

    # Remove the identified supersets or subsets
    return [patchCandidates[i] for i in range(len(patchCandidates)) if i not in to_remove]


def makeSumSets() -> set[tuple[int, ...]]:
    setLists = [list(s) for s in patchCandidates]

    # Use itertools.product for cartesian product
    all_combinations = product(*setLists)

    # Convert each combination to a sorted tuple of ints and collect in a set
    result_sets = {tuple(sorted(set(int(element) for element in combination))) for combination in all_combinations}

    return result_sets


def minPatches(nums: List[int], n: int) -> int:
    for i in range(n):
        addPatchCandidates(nums, i)
    answers = findCommon()
    for answer in answers:
        print(answer)

    return len(answers[0])


print(minPatches(LIST, N))
