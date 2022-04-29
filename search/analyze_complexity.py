from core import evaluate_test_case
from search.binary_search import locate_card
from search.linear_search import locate_card as locate_card_linear

large_test = {
    'input': {
        'cards': list(range(10000000, 0, -1)),
        'query': 2
    },
    'output': 9999998
}

result, passed, runtime = evaluate_test_case(locate_card_linear, large_test, display=False)
print(f"Result: {result}\nPassed: {passed}\nExecution Time: {runtime} ms")

result, passed, runtime = evaluate_test_case(locate_card, large_test, display=False)
print(f"\n\nResult: {result}\nPassed: {passed}\nExecution Time: {runtime} ms")
