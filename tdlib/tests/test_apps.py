import base
import sys
import tdlib
import unittest
import random
import printer

from graphs import *

#don't confuse python unittest
sys.argv=sys.argv[:1]

class TestTdLib_app(unittest.TestCase):
    def test_max_clique_with_treedecomposition_0a(self):
        V, E = cornercases[0]
        G = Graph(V, E)
        T, w = tdlib.PP_FI_TM(G)
        s, S = tdlib.max_clique_with_treedecomposition(G, T)
        self.assertEqual(len(S), 0)
        self.assertEqual(len(S), s)

    def test_max_clique_with_treedecomposition_0b(self):
        V, E = cornercases[1]
        G = Graph(V, E)
        T, w = tdlib.PP_FI_TM(G)
        s, S = tdlib.max_clique_with_treedecomposition(G, T)
        self.assertEqual(len(S), 1)
        self.assertEqual(len(S), s)

    def test_max_clique_with_treedecomposition_0c(self):
        V, E = cornercases[2]
        G = Graph(V, E)
        T, w = tdlib.PP_FI_TM(G)
        s, S = tdlib.max_clique_with_treedecomposition(G, T)
        self.assertEqual(len(S), 1)
        self.assertEqual(len(S), s)

    def test_max_clique_with_treedecomposition_0d(self):
        V, E = cornercases[3]
        G = Graph(V, E)
        T, w = tdlib.PP_FI_TM(G)
        s, S = tdlib.max_clique_with_treedecomposition(G, T)
        self.assertEqual(len(S), 5)
        self.assertEqual(len(S), s)

    def test_max_clique_with_treedecomposition_1(self):
        G = Graph(V_P6, E_P6)
        T, w = tdlib.PP_FI_TM(G)
        s, S = tdlib.max_clique_with_treedecomposition(G, T)
        self.assertEqual(len(S), 2)
        self.assertEqual(len(S), s)

    def test_max_clique_with_treedecomposition_3(self):
        G = Graph(V_Petersen, E_Petersen)
        T, w = tdlib.PP_FI_TM(G)
        s, S = tdlib.max_clique_with_treedecomposition(G, T)
        self.assertEqual(len(S), 2)
        self.assertEqual(len(S), s)

    def test_max_clique_with_treedecomposition_4(self):
        G = Graph(V_Petersen_double, E_Petersen_double)
        T, w = tdlib.PP_FI_TM(G)
        s, S = tdlib.max_clique_with_treedecomposition(G, T)
        self.assertEqual(len(S), 2)
        self.assertEqual(len(S), s)

    def test_max_clique_with_treedecomposition_5(self):
        G = Graph(V_Wagner, E_Wagner)
        T, w = tdlib.PP_FI_TM(G)
        s, S = tdlib.max_clique_with_treedecomposition(G, T)
        self.assertEqual(len(S), 2)
        self.assertEqual(len(S), s)

    def test_max_clique_with_treedecomposition_6(self):
        G = Graph(V_Pappus, E_Pappus)
        T, w = tdlib.PP_FI_TM(G)
        s, S = tdlib.max_clique_with_treedecomposition(G, T)
        self.assertEqual(len(S), 2)
        self.assertEqual(len(S), s)

    def test_max_clique_with_treedecomposition_7(self):
        G = Graph(V_Grid_5_5, E_Grid_5_5)
        T, w = tdlib.PP_FI_TM(G)
        s, S = tdlib.max_clique_with_treedecomposition(G, T)
        self.assertEqual(len(S), 2)
        self.assertEqual(len(S), s)

    def test_max_clique_with_treedecomposition_8(self):
        for n in range(0, 13):
            for i in range(0, 10):
                V, E = randomGNP(n, 0.2)
                G = Graph(V, E)
                T, w = tdlib.PP_FI_TM(G)
                s, S = tdlib.max_clique_with_treedecomposition(G, T)
                self.assertEqual(len(S), s)

    def test_max_independent_set_with_treedecomposition_0a(self):
        V, E = cornercases[0]
        G = Graph(V, E)
        T, w = tdlib.PP_FI_TM(G)
        s, S = tdlib.max_independent_set_with_treedecomposition(G, T)
        self.assertEqual(s, 0)
        self.assertEqual(len(S), s)

    def test_max_independent_set_with_treedecomposition_0b(self):
        V, E = cornercases[1]
        G = Graph(V, E)
        T, w = tdlib.PP_FI_TM(G)
        s, S = tdlib.max_independent_set_with_treedecomposition(G, T)
        self.assertEqual(s, 1)
        self.assertEqual(len(S), s)

    def test_max_independent_set_with_treedecomposition_0c(self):
        V, E = cornercases[2]
        G = Graph(V, E)
        T, w = tdlib.PP_FI_TM(G)
        s, S = tdlib.max_independent_set_with_treedecomposition(G, T)
        self.assertEqual(s, 5)
        self.assertEqual(len(S), s)

    def test_max_independent_set_with_treedecomposition_0d(self):
        V, E = cornercases[3]
        G = Graph(V, E)
        T, w = tdlib.PP_FI_TM(G)
        s, S = tdlib.max_independent_set_with_treedecomposition(G, T)
        self.assertEqual(s, 1)
        self.assertEqual(len(S), s)

    def test_max_independent_set_with_treedecomposition_1(self):
        G = Graph(V_P6, E_P6)
        T, w = tdlib.PP_FI_TM(G)
        s, S = tdlib.max_independent_set_with_treedecomposition(G, T)
        self.assertEqual(s, 3)
        self.assertEqual(len(S), s)

    def test_max_independent_set_with_treedecomposition_2(self):
        G = Graph(V_K5, E_K5)
        T, w = tdlib.PP_MD(G)
        s, S = tdlib.max_independent_set_with_treedecomposition(G, T)
        self.assertEqual(s, 1)
        self.assertEqual(len(S), s)

    def test_max_independent_set_with_treedecomposition_3(self):
        G = Graph(V_Petersen, E_Petersen)
        T, w = tdlib.PP_FI_TM(G)
        s, S = tdlib.max_independent_set_with_treedecomposition(G, T)
        self.assertEqual(s, 4)
        self.assertEqual(len(S), s)

    def test_max_independent_set_with_treedecomposition_4(self):
        G = Graph(V_Petersen_double, E_Petersen_double)
        T, w = tdlib.PP_MD(G)
        s, S = tdlib.max_independent_set_with_treedecomposition(G, T)
        self.assertEqual(s, 8)
        self.assertEqual(len(S), s)

    def test_max_independent_set_with_treedecomposition_5(self):
        G = Graph(V_Wagner, E_Wagner)
        T, w = tdlib.PP_FI_TM(G)
        s, S = tdlib.max_independent_set_with_treedecomposition(G, T)
        self.assertEqual(s, 3)
        self.assertEqual(len(S), s)

    def test_max_independent_set_with_treedecomposition_6(self):
        G = Graph(V_Pappus, E_Pappus)
        T, w = tdlib.PP_FI_TM(G)
        s, S = tdlib.max_independent_set_with_treedecomposition(G, T)
        self.assertEqual(s, 9)
        self.assertEqual(len(S), s)

    def test_max_independent_set_with_treedecomposition_7(self):
        G = Graph(V_Grid_5_5, E_Grid_5_5)
        T, w = tdlib.PP_FI_TM(G)
        s, S = tdlib.max_independent_set_with_treedecomposition(G, T)
        self.assertEqual(s, 13)
        self.assertEqual(len(S), s)

    def test_max_independent_set_with_treedecomposition_8(self):
        for n in range(0, 13):
            for i in range(0, 10):
                V, E = randomGNP(n, 0.2)
                G = Graph(V, E)
                T, w = tdlib.PP_FI_TM(G)
                s, S = tdlib.max_independent_set_with_treedecomposition(G, T)
                self.assertEqual(len(S), s)

    def test_min_vertex_cover_with_treedecomposition_0a(self):
        V, E = cornercases[0]
        G = Graph(V, E)
        T, w = tdlib.PP_FI_TM(G)
        s, S = tdlib.min_vertex_cover_with_treedecomposition(G, T)
        self.assertEqual(len(S), 0)
        self.assertEqual(len(S), s)

    def test_min_vertex_cover_with_treedecomposition_0b(self):
        V, E = cornercases[1]
        G = Graph(V, E)
        T, w = tdlib.PP_FI_TM(G)
        s, S = tdlib.min_vertex_cover_with_treedecomposition(G, T)
        self.assertEqual(len(S), 0)
        self.assertEqual(len(S), s)

    def test_min_vertex_cover_with_treedecomposition_0c(self):
        V, E = cornercases[2]
        G = Graph(V, E)
        T, w = tdlib.PP_FI_TM(G)
        s, S = tdlib.min_vertex_cover_with_treedecomposition(G, T)
        self.assertEqual(len(S), 0)
        self.assertEqual(len(S), s)

    def test_min_vertex_cover_with_treedecomposition_0d(self):
        V, E = cornercases[3]
        G = Graph(V, E)
        T,  w = tdlib.PP_FI_TM(G)
        s, S = tdlib.min_vertex_cover_with_treedecomposition(G, T)
        self.assertEqual(len(S), 4)
        self.assertEqual(len(S), s)

    def test_min_vertex_cover_with_treedecomposition_1(self):
        G = Graph(V_P6, E_P6)
        T, w = tdlib.PP_FI_TM(G)
        s, S = tdlib.min_vertex_cover_with_treedecomposition(G, T)
        self.assertEqual(len(S), 3)
        self.assertEqual(len(S), s)

    def test_min_vertex_cover_with_treedecomposition_2(self):
        G = Graph(V_K5, E_K5)
        T, w = tdlib.PP_FI_TM(G)
        s, S = tdlib.min_vertex_cover_with_treedecomposition(G, T)
        self.assertEqual(len(S), 4)
        self.assertEqual(len(S), s)

    def test_min_vertex_cover_with_treedecomposition_3(self):
        G = Graph(V_Petersen, E_Petersen)
        T, w = tdlib.PP_FI_TM(G)
        s, S = tdlib.min_vertex_cover_with_treedecomposition(G, T)
        self.assertEqual(len(S), 6)
        self.assertEqual(len(S), s)

    def test_min_vertex_cover_with_treedecomposition_4(self):
        G = Graph(V_Petersen_double, E_Petersen_double)
        T, w = tdlib.PP_FI_TM(G)
        s, S = tdlib.min_vertex_cover_with_treedecomposition(G, T)
        self.assertEqual(len(S), 12)
        self.assertEqual(len(S), s)

    def test_min_vertex_cover_with_treedecomposition_5(self):
        G = Graph(V_Wagner, E_Wagner)
        T, w = tdlib.PP_FI_TM(G)
        s, S = tdlib.min_vertex_cover_with_treedecomposition(G, T)
        self.assertEqual(len(S), 5)
        self.assertEqual(len(S), s)

    def test_min_vertex_cover_with_treedecomposition_6(self):
        G = Graph(V_Pappus, E_Pappus)
        T, w = tdlib.PP_FI_TM(G)
        s, S = tdlib.min_vertex_cover_with_treedecomposition(G, T)
        self.assertEqual(len(S), 9)
        self.assertEqual(len(S), s)

    def test_min_vertex_cover_with_treedecomposition_7(self):
        G = Graph(V_Grid_5_5, E_Grid_5_5)
        T, w = tdlib.PP_FI_TM(G)
        s, S = tdlib.min_vertex_cover_with_treedecomposition(G, T)
        self.assertEqual(len(S), 12)
        self.assertEqual(len(S), s)

    def test_min_vertex_cover_with_treedecomposition_8(self):
        for n in range(0, 13):
            for i in range(0, 10):
                V, E = randomGNP(n, 0.2)
                G = Graph(V, E)
                T, w = tdlib.PP_FI_TM(G)
                s, S = tdlib.min_vertex_cover_with_treedecomposition(G, T)
                self.assertEqual(len(S), s)
                self.assertEqual(len(S), s)

    def test_min_dominating_set_with_treedecomposition_0a(self):
        V, E = cornercases[0]
        G = Graph(V, E)
        T, w = tdlib.PP_MD(G)
        s, S = tdlib.min_dominating_set_with_treedecomposition(G, T)
        self.assertEqual(len(S), 0)
        self.assertEqual(len(S), s)

    def test_min_dominating_set_with_treedecomposition_0b(self):
        V, E = cornercases[1]
        G = Graph(V, E)
        T, w = tdlib.PP_MD(G)
        s, S = tdlib.min_dominating_set_with_treedecomposition(G, T)
        self.assertEqual(len(S), 1)
        self.assertEqual(len(S), s)

    def test_min_dominating_set_with_treedecomposition_0c(self):
        V, E = cornercases[2]
        G = Graph(V, E)
        T, w = tdlib.PP_MD(G)
        s, S = tdlib.min_dominating_set_with_treedecomposition(G, T)
        self.assertEqual(len(S), 5)
        self.assertEqual(len(S), s)

    def test_min_dominating_set_with_treedecomposition_0d(self):
        V, E = cornercases[3]
        G = Graph(V, E)
        T, w = tdlib.PP_MD(G)
        s, S = tdlib.min_dominating_set_with_treedecomposition(G, T)
        self.assertEqual(len(S), 1)
        self.assertEqual(len(S), s)

    def test_min_dominating_set_with_treedecomposition_1(self):
        G = Graph(V_P6, E_P6)
        T, w = tdlib.PP_MD(G)
        s, S = tdlib.min_dominating_set_with_treedecomposition(G, T)
        self.assertEqual(len(S), 2)
        self.assertEqual(len(S), s)

    def test_min_dominating_set_with_treedecomposition_2(self):
        G = Graph(V_K5, E_K5)
        T, w = tdlib.PP_MD(G)
        s, S = tdlib.min_dominating_set_with_treedecomposition(G, T)
        self.assertEqual(len(S), 1)
        self.assertEqual(len(S), s)

    def test_min_dominating_set_with_treedecomposition_3(self):
        G = Graph(V_Petersen, E_Petersen)
        T, w = tdlib.PP_MD(G)
        s, S = tdlib.min_dominating_set_with_treedecomposition(G, T)
        self.assertEqual(len(S), 3)
        self.assertEqual(len(S), s)

    def test_min_dominating_set_with_treedecomposition_4(self):
        G = Graph(V_Petersen_double, E_Petersen_double)
        T, w = tdlib.PP_MD(G)
        s, S = tdlib.min_dominating_set_with_treedecomposition(G, T)
        self.assertEqual(len(S), 6)
        self.assertEqual(len(S), s)

    def test_min_dominating_set_with_treedecomposition_5(self):
        G = Graph(V_Wagner, E_Wagner)
        T, w = tdlib.PP_MD(G)
        s, S = tdlib.min_dominating_set_with_treedecomposition(G, T)
        self.assertEqual(len(S), 3)
        self.assertEqual(len(S), s)

    def test_min_dominating_set_with_treedecomposition_6(self):
        G = Graph(V_Pappus, E_Pappus)
        T, w = tdlib.PP_MD(G)
        s, S = tdlib.min_dominating_set_with_treedecomposition(G, T)
        self.assertEqual(len(S), 5)
        self.assertEqual(len(S), s)

    def test_min_dominating_set_with_treedecomposition_7(self):
        G = Graph(V_Grid_5_5, E_Grid_5_5)
        T, w = tdlib.PP_MD(G)
        s, S = tdlib.min_dominating_set_with_treedecomposition(G, T)
        self.assertEqual(len(S), 7)
        self.assertEqual(len(S), s)

    def test_min_dominating_set_with_treedecomposition_8(self):
        for n in range(0, 13):
            for i in range(0, 10):
                V, E = randomGNP(n, 0.2)
                G = Graph(V, E)
                T, w = tdlib.PP_MD(G)
                s, S = tdlib.min_dominating_set_with_treedecomposition(G, T)
                self.assertEqual(len(S), s)

    def test_min_coloring_with_treedecomposition_0a(self):
        V, E = cornercases[0]
        G = Graph(V, E)
        T, w = tdlib.PP_MD(G)
        s, S = tdlib.min_coloring_with_treedecomposition(G, T)
        self.assertEqual(len(S), 0)
        self.assertEqual(len(S), s)

    def test_min_coloring_with_treedecomposition_0b(self):
        V, E = cornercases[1]
        G = Graph(V, E)
        T, w = tdlib.PP_MD(G)
        s, S = tdlib.min_coloring_with_treedecomposition(G, T)
        self.assertEqual(len(S), 1)
        self.assertEqual(len(S), s)

    def test_min_coloring_with_treedecomposition_0c(self):
        V, E = cornercases[2]
        G = Graph(V, E)
        T, w = tdlib.PP_MD(G)
        s, S = tdlib.min_coloring_with_treedecomposition(G, T)
        self.assertEqual(len(S), 1)
        self.assertEqual(len(S), s)

    def test_min_coloring_with_treedecomposition_0d(self):
        V, E = cornercases[3]
        G = Graph(V, E)
        T, w = tdlib.PP_MD(G)
        s, S = tdlib.min_coloring_with_treedecomposition(G, T)
        self.assertEqual(len(S), 5)
        self.assertEqual(len(S), s)

    def test_min_coloring_with_treedecomposition_1(self):
        G = Graph(V_P6, E_P6)
        T, w = tdlib.PP_MD(G)
        s, S = tdlib.min_coloring_with_treedecomposition(G, T)
        self.assertEqual(len(S), 2)
        self.assertEqual(len(S), s)

    def test_min_coloring_with_treedecomposition_2(self):
        G = Graph(V_K5, E_K5)
        T, w = tdlib.PP_MD(G)
        s, S = tdlib.min_coloring_with_treedecomposition(G, T)
        self.assertEqual(len(S), 5)
        self.assertEqual(len(S), s)

    def test_min_coloring_with_treedecomposition_3(self):
        G = Graph(V_Petersen, E_Petersen)
        T, w = tdlib.PP_MD(G)
        s, S = tdlib.min_coloring_with_treedecomposition(G, T)
        self.assertEqual(len(S), 3)
        self.assertEqual(len(S), s)

    def test_min_coloring_with_treedecomposition_4(self):
        G = Graph(V_Petersen_double, E_Petersen_double)
        T, w = tdlib.PP_MD(G)
        s, S = tdlib.min_coloring_with_treedecomposition(G, T)
        self.assertEqual(len(S), 3)
        self.assertEqual(len(S), s)

    def test_min_coloring_with_treedecomposition_5(self):
        G = Graph(V_Wagner, E_Wagner)
        T, w = tdlib.PP_MD(G)
        s, S = tdlib.min_coloring_with_treedecomposition(G, T)
        self.assertEqual(len(S), 3)
        self.assertEqual(len(S), s)

    def test_min_coloring_with_treedecomposition_6(self):
        G = Graph(V_Pappus, E_Pappus)
        T, w = tdlib.PP_MD(G)
        s, S = tdlib.min_coloring_with_treedecomposition(G, T)
        self.assertEqual(len(S), 2)
        self.assertEqual(len(S), s)

    def test_min_coloring_with_treedecomposition_7(self):
        G = Graph(V_Grid_5_5, E_Grid_5_5)
        T, w = tdlib.PP_MD(G)
        s, S = tdlib.min_coloring_with_treedecomposition(G, T)
        self.assertEqual(len(S), 2)
        self.assertEqual(len(S), s)

    def test_min_coloring_with_treedecomposition_8(self):
        for n in range(0, 13):
            for i in range(0, 10):
                V, E = randomGNP(n, 0.2)
                G = Graph(V, E)
                T, w = tdlib.PP_MD(G)
                s, S = tdlib.min_coloring_with_treedecomposition(G, T)
                self.assertEqual(len(S), s)

if __name__ == '__main__':
    unittest.main()
