from scipy.sparse import csr_matrix
import numpy as np
from scipy.sparse.csgraph import csgraph_from_dense

G_dense = np.array([ [0, 2, 1],
                     [2, 0, 0],
                     [1, 0, 0] ])
                     
G_masked = np.ma.masked_values(G_dense, 0)

G_sparse = csr_matrix(G_dense)
print (G_sparse.data)


G2_data = np.array
([
   [np.inf, 2, 0 ],
   [2, np.inf, np.inf],
   [0, np.inf, np.inf]
])
# G2_masked = np.ma.masked_invalid(G2_data)
G2_sparse = csgraph_from_dense(G2_data, null_value=np.inf, infinity_null=False, nan_null=False)
print (G2_sparse.data)