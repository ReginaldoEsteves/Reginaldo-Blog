import numpy as np
import pandas as pd
from plotnine import (
    ggplot, aes, geom_point, geom_abline, ggsave
)

X = np.loadtxt(r"c:\Users\Vitor\Desktop\Reginaldo\Work3\X.txt")
y = np.loadtxt(r"c:\Users\Vitor\Desktop\Reginaldo\Work3\y.txt")


X_design = np.column_stack((np.ones_like(X), X))


beta = np.linalg.inv(X_design.T @ X_design) @ (X_design.T @ y)

a = beta[0]   
b = beta[1]   

print("Intercepto (a):", a)
print("Inclinação (b):", b)


df = pd.DataFrame({"x": X, "y": y})

plot = (
    ggplot(df, aes("x", "y"))
    + geom_point()                        
    + geom_abline(intercept=a, slope=b)   
)


plot.save("grafico.png")

print("Gráfico salvo como grafico.png")
