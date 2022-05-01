# Business-dashboard


## Table of contents

- [Overview](#overview)
  - [The challenge](#the-challenge)
  - [Links](#links)
- [My process](#my-process)
  - [Built with](#built-with)
  - [What I learned](#what-i-learned)
  - [Continued development](#continued-development)
  - [Useful resources](#useful-resources)
- [Author](#author)


## Overview

### The challenge

This is a solution a business analytics dashboard for a mini-mart. The mini-mart started in 2020 to date due to human error and faulty pos system the sales report generated didn't show the sales well.




### Links

- Solution URL: [My solution](https://github.com/kariswanjiru/jiamini_project/)
- Live demo URL : [Web App](https://jiamini-app.herokuapp.com/)

## My process

### Built with

- Pandas
- Numpy
- Skit-learn
- Matplotlib

### What I learned

I learnt how to use stratified k-folds to better the accuracy of my machine learning algorithm and using concat to join two datasets.

This is a code snippet of what i learnt, see below:

```python
i = 1 
kf = StratifiedKFold(n_splits=5,random_state=1,shuffle=True)
for train_index,test_index in kf.split(x , y):
    print('{} of kfold {}'.format(i,kf.n_splits))
    xtr,xvl = x.iloc[train_index],x.iloc[test_index]
    ytr,yvl = y.iloc[train_index],y.iloc[test_index]
    model = LogisticRegression(random_state=1)
    model.fit(xtr,ytr)
    pred_test = model.predict(xvl)
    score = accuracy_score(yvl,pred_test)
    print('accuracy_score',score)
    i+=1
    pred_test = model.predict(test)
    pred = model.predict_proba(xvl)[:, 1]
    
```
```python
 pd.concat([df1,df2])
```

### Continued development
A better UI for the dashboard will be created using react js and flask. To improve accuracy better KPI's for business intelligence dashboardswill be used in combination with boosting algorithms like Ada Boost to improve forecasting.

### Useful resources

- [Skit-learn](https://scikit-learn.org/stable/) - This helped me with deeper understanding of the use of skit-lern models.
- [Pandas](https://pandas.pydata.org/docs/) - Pandas docuentation.



## Author

- LinkedIn - [Wanjiru Kariuki](https://www.linkedin.com/in/wanjiru-kariuki/)
- Twitter - [@Wanjiruestar](https://www.twitter.com/Wanjiruestar)

