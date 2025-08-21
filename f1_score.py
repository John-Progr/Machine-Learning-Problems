y_true = [1, 0, 1, 1, 0]
y_pred = [1, 0, 0, 1, 1]

TP = FP = TN = FN = 0

for yt, yp in zip(y_true, y_pred):
    if yt == 1 and yp == 1:
        TP += 1
    elif yt == 0 and yp == 1:
        FP += 1
    elif yt == 0 and yp == 0:
        TN += 1
    elif yt == 1 and yp == 0:
        FN += 1
        
  
Precision = TP / (TP + FP)
Recall = TP / (TP + FN)

F1 = 2 * (Precision * Recall) / (Precision + Recall)

print(F1)
print("TP:", TP, "FP:", FP, "TN:", TN, "FN:", FN)
