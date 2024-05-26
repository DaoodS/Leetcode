def merge(arr):

    inter = [-1]*len(arr)

    for i in range(len(arr)-2):
        for j in range(i+1, len(arr)-1):
            if arr[j][0]<=arr[i][0] or arr[j][1]>=arr[i][1]:
                print(i,j,inter) 
                if inter[i]==-1:
                    inter[i] = [min(arr[i][0], arr[j][0]), max(arr[i][1], arr[j][1])]
                elif arr[j][0]<=inter[i][0] or arr[j][1]>=inter[i][1]:
                    inter[i][0] = min(inter[i][0], arr[j][0])
                    inter[i][1] = max(inter[i][1], arr[j][1])

    finalarr = []
    for i in range(len(inter)-1):
        if inter[i]!=-1:
            finalarr.append(inter[i])

    return finalarr

            
print(merge([[1,3],[2,4],[6,8],[9,10]]))
