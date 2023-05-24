import json
from display import HEADER
from ledger import Ledger, LedgerEncoder
# from tasks import Task


def main():
    ledger = Ledger()
    keys = ('title', 'importance', 'duration', 'desc')
    args1 = ('dishes', None, None, 'do them')
    args2 = ('vaccuum', 5, 15, 'do it')
    # task1 = Task(*args1)
    # print(task1)

    d1 = dict(zip(keys, args1))
    d2 = dict(zip(keys, args2))

    ledger.add_task(**d1)
    ledger.add_task(**d2)
    padding = '\n' + ' ' * 20
    print(padding.join(s for s in HEADER))

    print(ledger)
    print(json.dumps(ledger, cls=LedgerEncoder, indent=2))


if __name__ == "__main__":
    main()
