cd C:\Users\Prateek\PycharmProjects\Sprint2
behave -f allure_behave.formatter:AllureFormatter -o ./allure_reports features/ClothProduct.feature
behave --junit --junit-directory junitreports features/ClothProduct.feature
behave -f json.pretty -o jreports features/ClothProduct.feature