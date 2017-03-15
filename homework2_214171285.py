import nsfg
import thinkplot
import thinkstats2
pres = nsfg.ReadFemResp()
width=0.5
#Q1
fmar1age = pres['fmar1age']
histog1= thinkstats2.Hist(fmar1age)
pres.fmar1age.value_counts().sort_index()
thinkplot.Hist(histog1,width=width)
thinkplot.config(xlabel="The age during the first marraige",ylabel = "The Frequency")
#Q2
fmarno = pres['fmarno']
histog2 = thinkstats2.Hist(fmarno)
pres.fmarno.value_counts().sort_index()
thinkplot.Hist(histog2,width=width)
thinkplot.config(xlabel='Number of Marriages', ylabel='Number of Frequency')
#Q3
totincr = pres['totincr']
histo3 = thinkstats2.Hist(totincr)
pres.totincr.value_counts().sort_index()
thinkplot.Hist(histo3,width=width) 
thinkplot.config(xlabel="Range",ylabel = "Frequency")
#Q4
neverMarried = pres[pres.fmarno == 0]
married = pres[pres.fmarno >= 1]

histog4 = thinkstats2.Hist(neverMarried.totincr, label="Never Married")
histog5 = thinkstats2.Hist(married.totincr, label="Married")
thinkplot.Hist(histog4,width=width)
thinkplot.Hist(histog5,width=width)
thinkplot.config(xlabel='Time', ylabel='Amount',)
#Q5

min_nevermarried=neverMarried.totincr.min()
max_nevermarried=neverMarried.totincr.max()
std_nevermarried=neverMarried.totincr.std()
var_nevermarried=neverMarried.totincr.var()
mean_nevermarried=neverMarried.totincr.mean()
min_married=married.totincr.min()
max_married=married.totincr.max()
std_married=married.totincr.std()
var_married=married.totincr.var()
mean_married=married.totincr.mean()


print 'Miminum value of total income of never married respondents is %.2f' %min_nevermarried
print 'Maximum value of total income of never married respondents is %.2f' %max_nevermarried
print 'Standart deviation of total income of never married respondents is %.2f' %std_nevermarried
print 'Varience of total income of never married respondents is %.2f' %var_nevermarried
print 'Mean of total income of never married respondents is %.2f' %mean_nevermarried

print 'Miminum value of total income of married respondents is %.2f' %min_married
print 'Maximum value of total income of married respondents is %.2f' %max_married
print 'Standart deviation of total income of married respondents is %.2f' %std_married
print 'Varience of total income of married respondents is %.2f' %var_married
print 'Mean of total income of married respondents is %.2f' %mean_married
