from conversion import json_to_dict
def check_symmetry(data:dict):
    y = data['y']['y1']
    avg = sum(y)/len(y)
    new_y = [i-avg for i in y]
    y = sorted(new_y)
    h = [(i+1)*100/len(y) for i in range(len(y))]
    negative_h = []
    for i in range(len(y)):
        nyi = -y[i]
        k=0
        for j in range(len(y)):
            if nyi > y[i]:
                k+=1
        negative_h.append((1-k)/len(y))
    w2 = [(h[i]+negative_h[i]-1)**2 for i in range(len(y))]
    sum_w2 = sum(w2)/len(w2)
    print(sum_w2)
    print(max(w2))
    return w2
def main():
    data = json_to_dict('func_y1.json')
    res = check_symmetry(data)
    print(res)

if __name__ == '__main__':
    main()