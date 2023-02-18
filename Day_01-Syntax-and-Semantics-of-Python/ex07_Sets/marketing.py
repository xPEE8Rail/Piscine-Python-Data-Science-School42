import sys


def set_funct():
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com', 'john@snow.is', 'bill_gates@live.com',
               'mark@facebook.com', 'elon@paypal.com', 'jessica@gmail.com']
    participants = ['walter@heisenberg.com', 'vasily@mail.ru', 'pinkman@yo.org', 'jessica@gmail.com',
                    'elon@paypal.com', 'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']
    return set(clients), set(participants), set(recipients)


def call_center(clients_set, recipients_set):
    a = clients_set.difference(recipients_set)
    return list(a)


def potential_clients(participants_set, clients_set):
    b = participants_set.difference(clients_set)
    return list(b)


def loyalty_program(clients_set, participants_set):
    c = clients_set.difference(participants_set)
    return list(c)


def marketing():
    sets = set_funct()
    if sys.argv[1] == "call_center":
        return call_center(sets[0], sets[2])
    elif sys.argv[1] == "potential_clients":
        return call_center(sets[1], sets[0])
    elif sys.argv[1] == "loyalty_program":
        return call_center(sets[0], sets[1])
    else:
        raise ValueError('Invalid argument')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(marketing())
