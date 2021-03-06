% Reading the data from the csv file in the form of table
clear; clc;
T = readtable('LinearRegressionData.csv');
%%
% Using Ordinary Least Squares approach to find the best fit line
y = T.GPA; % GPA scores data
x = T.SAT; % SAT scores data

one = ones(84,1);
X = [x one];

parameters = pinv(X'*X)*(X'*y); % (X^T * X)^-1 * X^T * y

scatter(x,y); hold on;

Y = parameters(1)*x+parameters(2)*one;

plot(x,Y);
legend("Data","Fitted Line")
xlabel("SAT")
ylabel("GPA")

print -dpng Result_using_MyOLS 

