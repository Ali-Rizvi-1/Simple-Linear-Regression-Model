% Reading the data from the csv file in the form of table

T = readtable('LinearRegressionData.csv');
%%
% Using Ordinary Least Squares approach to find the best fit line
y = T.GPA(:,1); % GPA scores data
x = T.SAT(:,1); % SAT scores data

one = ones(84,1);
X = [x one];

temp = pinv(X'*X); 
temp2 = X'*y;
parameters = temp*temp2; % (X^T * X)^-1 * X^T * y

scatter(x,y); hold on;

Y = parameters(1)*x+parameters(2)*one;

plot(x,Y);
legend("Data","Fitted Line")
xlabel("SAT")
ylabel("GPA")


