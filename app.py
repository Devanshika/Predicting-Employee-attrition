
from tkinter import *
from login import Login, Register
from PIL import Image, ImageTk
from ResultPredictor import ResultPredictor


class MainWindow:
    def __init__(self):
        self.result_predictor = ResultPredictor("processed_data.csv")
        self.app = Tk()
        self.app.title("Predicting Employee Attrition")
        self.app.geometry("1000x600")
        self.app['background'] = '#abbfd1'
        self.logo = Image.open('logo.jpg')
        self.logo = ImageTk.PhotoImage(self.logo)
        self.logo_label = Label(image=self.logo)
        self.logo_label.image = self.logo
        self.logo_label.place(x=300, y=125)
        self.label = Label(
            self.app, text="Please Login/Register to continue..", font="calibri")
        self.label.place(x=370, y=10)
        self.loginBtn = Button(self.app, text="LOGIN",
                               pady=5, fg="blue", padx=100, command=self.login)
        self.loginBtn.place(x=30, y=250)
        self.registerBtn = Button(
            self.app, text="REGISTER", fg="blue", pady=5, padx=100, command=self.register)
        self.registerBtn.place(x=30, y=300)

    def login_successful(self):
        self.app.destroy()
        self.app = Tk()
        self.app.title("Predicting Employee Attrition")
        self.app.geometry("1600x900")
        self.app['background'] = '#abbfd1'
        self.fillForm()
        self.run()

    def fillForm(self):
        l1 = Label(self.app, text='Input Data', bg='black',
                   fg='yellow', font=("bold", 30))
        l1.pack(fill=X)
        Label(self.app, text="Age").place(x=30, y=100)
        Label(self.app, text="Business Travels").place(x=30, y=150)
        Label(self.app, text="Daily Rate").place(x=30, y=200)
        Label(self.app, text="Department").place(x=30, y=250)
        Label(self.app, text="Distance from Home").place(x=30, y=300)
        Label(self.app, text="Education").place(x=30, y=350)
        Label(self.app, text="Education Field").place(x=30, y=400)
        Label(self.app, text="Environment Satisfaction").place(x=30, y=450)
        Label(self.app, text="Gender").place(x=30, y=500)
        Label(self.app, text="Hourly Rate").place(x=30, y=550)
        Label(self.app, text="Job Involvement").place(x=30, y=600)
        Label(self.app, text="Job Level").place(x=30, y=650)
        Label(self.app, text="Job Role").place(x=30, y=700)
        Label(self.app, text="Job Satisfaction").place(x=30, y=750)
        Label(self.app, text="Marital Status").place(x=30, y=800)
        Label(self.app, text="Monthly Income").place(x=630, y=100)
        Label(self.app, text="Monthly Rate").place(x=630, y=150)
        Label(self.app, text="Number of Companies Worked").place(x=630, y=200)
        Label(self.app, text="Overtime").place(x=630, y=250)
        Label(self.app, text="Salary Hike Percentage").place(x=630, y=300)
        Label(self.app, text="Performance Rating").place(x=630, y=350)
        Label(self.app, text="Relationship Satisfaction").place(x=630, y=400)
        Label(self.app, text="Stock Option Level").place(x=630, y=450)
        Label(self.app, text="Total Working Years").place(x=630, y=500)
        Label(self.app, text="Training Times Last Year").place(x=630, y=550)
        Label(self.app, text="Work Life Balance").place(x=630, y=600)
        Label(self.app, text="Years at Company").place(x=630, y=650)
        Label(self.app, text="Years in Current Role").place(x=630, y=700)
        Label(self.app, text="Years since last Promotion").place(x=630, y=750)
        Label(self.app, text="Years with Current Manager").place(x=630, y=800)

        Label(self.app, text="Choose Model").place(x=1100, y=100)
        self.text = StringVar()
        self.text.set("Regularization Parameter")
        self.index = 1
        self.models = ["Logistic Regression", "Support Vector Machine",
                       "Random Forest", "K- Nearest Neighbors"]
        self.modelparameterLabels = [
            "Regularization Parameter", "Regularization Parameter", "Number of Estimators", "Number of Neighbors"]
        variable = StringVar(self.app)
        variable.set(self.models[0])
        dropdown = OptionMenu(self.app, variable, *self.models,
                              command=self.updateModelParamterLabel)
        dropdown.config(font=('Helvetica', 12))
        dropdown.place(x=1200, y=100)

        self.label = Label(
            self.app, textvariable=self.text).place(x=1100, y=550)
        self.labelEntry = Entry(self.app)
        self.labelEntry.place(x=1300, y=550)

        submitBtn = Button(self.app, text="Submit", width=10,
                           command=self.predictResult)
        submitBtn.place(x=1500, y=750)
        self.inputData = {'Age': Entry(self.app),
                          'BusinessTravel': Entry(self.app),
                          'DailyRate': Entry(self.app),
                          'Department': Entry(self.app),
                          'DistanceFromHome': Entry(self.app),
                          'Education': Entry(self.app),
                          'EducationField': Entry(self.app),
                          'EnvironmentSatisfaction': Entry(self.app),
                          'Gender': Entry(self.app),
                          'HourlyRate': Entry(self.app),
                          'JobInvolvement': Entry(self.app),
                          'JobLevel': Entry(self.app),
                          'JobRole': Entry(self.app),
                          'JobSatisfaction': Entry(self.app),
                          'MaritalStatus': Entry(self.app),
                          'MonthlyIncome': Entry(self.app),
                          'MonthlyRate':  Entry(self.app),
                          'NumCompaniesWorked': Entry(self.app),
                          'OverTime':  Entry(self.app),
                          'PercentSalaryHike': Entry(self.app),
                          'PerformanceRating':  Entry(self.app),
                          'RelationshipSatisfaction': Entry(self.app),
                          'StockOptionLevel': Entry(self.app),
                          'TotalWorkingYears': Entry(self.app),
                          'TrainingTimesLastYear': Entry(self.app),
                          'WorkLifeBalance': Entry(self.app),
                          'YearsAtCompany':  Entry(self.app),
                          'YearsInCurrentRole': Entry(self.app),
                          'YearsSinceLastPromotion': Entry(self.app),
                          'YearsWithCurrManager': Entry(self.app)
                          }
        self.inputData['Age'].place(x=330, y=100)
        self.inputData['BusinessTravel'].place(x=330, y=150)
        self.inputData['DailyRate'].place(x=330, y=200)
        self.inputData['Department'].place(x=330, y=250)
        self.inputData['DistanceFromHome'].place(x=330, y=300)
        self.inputData['Education'].place(x=330, y=350)
        self.inputData['EducationField'].place(x=330, y=400)
        self.inputData['EnvironmentSatisfaction'].place(x=330, y=450)
        self.inputData['Gender'].place(x=330, y=500)
        self.inputData['HourlyRate'].place(x=330, y=550)
        self.inputData['JobInvolvement'].place(x=330, y=600)
        self.inputData['JobLevel'].place(x=330, y=650)
        self.inputData['JobRole'].place(x=330, y=700)
        self.inputData['JobSatisfaction'].place(x=330, y=750)
        self.inputData['MaritalStatus'].place(x=330, y=800)
        self.inputData['MonthlyIncome'].place(x=930, y=100)
        self.inputData['MonthlyRate'].place(x=930, y=150)
        self.inputData['NumCompaniesWorked'].place(x=930, y=200)
        self.inputData['OverTime'].place(x=930, y=250)
        self.inputData['PercentSalaryHike'].place(x=930, y=300)
        self.inputData['PerformanceRating'].place(x=930, y=350)
        self.inputData['RelationshipSatisfaction'].place(x=930, y=400)
        self.inputData['StockOptionLevel'].place(x=930, y=450)
        self.inputData['TotalWorkingYears'].place(x=930, y=500)
        self.inputData['TrainingTimesLastYear'].place(x=930, y=550)
        self.inputData['WorkLifeBalance'].place(x=930, y=600)
        self.inputData['YearsAtCompany'].place(x=930, y=650)
        self.inputData['YearsInCurrentRole'].place(x=930, y=700)
        self.inputData['YearsSinceLastPromotion'].place(x=930, y=750)
        self.inputData['YearsWithCurrManager'].place(x=930, y=800)

    def updateModelParamterLabel(self, value):
        self.index= self.models.index(value)
        parametervalue= self.modelparameterLabels[self.index]
        self.text.set(parametervalue)

    def predictResult(self):
        data = {}
        for parameter in self.inputData:
            value = self.inputData[parameter].get()
            if(value == ""):
                value = None
            else:
                value = int(value)
            data[parameter] = value
        label_value=self.labelEntry.get()
        output = self.result_predictor.predict_result(self.index, label_value, data)
        self.app.destroy()
        self.createResultPage(output)

    def createResultPage(self,output):
        self.app = Tk()
        self.app.title("Predicting Employee Attrition")
        self.app.geometry("1000x1000")
        self.app['background'] = '#abbfd1'
        l1 = Label(self.app, text='Results', bg='white',
                   fg='blue', font=("bold", 30))
        l1.pack(fill=X)
        Label(self.app, text="The prediction for employee attrition is " + output['prediction'], font="calibri",fg='red').place(x=100,y=100)
        Label(self.app, text="The accuracy of the model is " + str(output['accuracy']), font="calibri",fg='green').place(x=100,y=150)
        x=100
        y=200
        dif = 30
        Label(self.app,text="Feature Importance",font="calibri").place(x=x,y=y)
        y=y+dif
        for feature in output['feature_importance']:
            if output['feature_importance'][feature]['importance'] > 0.01:
                Label(self.app, text=feature + " : " + str(output['feature_importance'][feature]['importance'])\
                    , font="calibri").place(x=x,y=y)
                if y < 700:
                    y=y+dif
                else:
                    x=x+dif*8
                    y = 230
        y = y + 100
        x = x + dif
        Button(self.app, text="Back to Input",pady=5, fg="blue", padx=100, command=self.login_successful).place(x=x,y=y)
        self.run()

    def run(self):
        self.app.mainloop()

    def login(self):
        loginTk= Login(self)
        loginTk.run()

    def register(self):
        registerTk= Register(self)
        registerTk.run()


app= MainWindow()
app.run()
