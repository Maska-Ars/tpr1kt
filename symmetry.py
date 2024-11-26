from conversion import json_to_dict


def check_symmetry(y: list[float]):

    y = sorted(y)

    h = [(i+1)/len(y) for i in range(len(y))]

    negative_h = []

    for i in range(len(y)):
        nyi = -y[i]
        k = 0
        for j in range(len(y)):
            if nyi > y[j]:
                k += 1
        negative_h.append(k/len(y))

    w2 = [(h[i]+negative_h[i]-1)**2 for i in range(len(y))]
    return sum(w2)


def main():
    data = json_to_dict('func_y1.json')
    res = check_symmetry(data)
    print(res)

if __name__ == '__main__':
    main()