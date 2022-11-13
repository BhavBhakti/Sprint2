cd C:\Users\Prateek\.jenkins\workspace\Sprint-Flip
behave -f allure_behave.formatter:AllureFormatter -o ./allure_reports features/ClothProduct.feature
behave --junit --junit-directory junit_reports features/ClothProduct.feature
behave -f json.pretty -o json_reports features/ClothProduct.feature