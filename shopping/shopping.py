import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    evi=[]
    label=[]
    month={
        'Jan':0,
        'Feb':1,
        'Mar':2,
        'Apr':3,
        'May':4,
        'June':5,
        'Jul':6,
        'Aug':7,
        'Sep':8,
        'Oct':9,
        'Nov':10,
        'Dec':11,
    }
    with open(f'{filename}',encoding='utf-8') as f:
        reader=csv.reader(f)
        next(reader)

        for i in reader:
            evi.append(i[:-1])
            label.append(i[-1])

        for i in evi:
            for j in range(len(i)):
                if j in [0,2,4,11,12,13,14]:
                    i[j]=int(i[j])
                elif j in [1,3,5,6,7,8,9]:
                    i[j]=float(i[j])
                elif j==10:
                    i[j]=month[i[j]]
                elif j==15:
                    if i[j]=='Returning_Visitor':
                        i[j]=1
                    else:
                        i[j]=0
                elif j==16:
                    if i[j]=='TRUE':
                        i[j]=1
                    else:
                        i[j]=0

        for i in range(len(label)):
            if label[i]=='TRUE':
                label[i]=1
            else:
                label[i]=0
    return (evi,label)


def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    n=KNeighborsClassifier(n_neighbors=1)
    return n.fit(evidence,labels)


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    sensi=0
    speci=0
    posi=0
    nega=0
    for i in range(len(labels)):
        if labels[i]==predictions[i]:
            if labels[i]==1:
                sensi+=1
            else:
                speci+=1
        if labels[i]==1:
            posi+=1
        if labels[i]==0:
            nega+=1
    return (sensi/posi,speci/nega)
        



if __name__ == "__main__":
    main()
