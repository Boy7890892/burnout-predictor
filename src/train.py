from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def train_logistic_regression(X_train, y_train):
    model = LogisticRegression(random_state=42)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    report = classification_report(y_test, predictions, target_names=['Aman (0)', 'Burnout (1)'])
    conf_matrix = confusion_matrix(y_test, predictions)
    
    print("====== HASIL EVALUASI MODEL AI ======")
    print(f"Akurasi Model: {accuracy:.2%}\n")
    print("Detail Klasifikasi (Precision, Recall, F1-Score):")
    print(report)
    print("Confusion Matrix:")
    print(conf_matrix)
    print("=====================================")
    return accuracy
