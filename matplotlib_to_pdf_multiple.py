import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
year = [1960, 1970, 1980, 1990, 2000, 2010]
pop_pakistan = [44.91, 58.09, 78.07, 107.7, 138.5, 170.6]
pop_india = [449.48, 553.57, 696.783, 870.133, 1000.4, 1309.1]
fig1 = plt.figure()
plt.plot(year, pop_pakistan, color='green')
plt.plot(year, pop_india, color='orange')
plt.xlabel('Countries')
plt.ylabel('Population in million')
plt.title('Pakistan India Population till 2010')
#plt.show()
fig2 = plt.figure()
x = [2, 4, 6]
y = [1, 3, 5]
plt.plot(x, y)
#plt.show()
pp = PdfPages(r'c:\temp\output.pdf')
pp.savefig(fig1)
pp.savefig(fig2)
pp.close()