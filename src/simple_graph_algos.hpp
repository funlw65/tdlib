// Lukas Larisch, 2014 - 2015
//
// (c) 2014-2015 Goethe-Universität Frankfurt
//
// This program is free software; you can redistribute it and/or modify it
// under the terms of the GNU General Public License as published by the
// Free Software Foundation; either version 2, or (at your option) any
// later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program; if not, write to the Free Software
// Foundation, 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
//
//
// Offers functionality to compute the connected components of a graph,
// vertex/edge deletion and other simple operations on graphs.
//

#ifndef TD_SIMPLE_GRAPH_ALGOS
#define TD_SIMPLE_GRAPH_ALGOS

namespace treedec{

#include <set>

#include <boost/graph/adjacency_list.hpp>

#include "graph.hpp"

//This function is used in the minimalChordal algorithm.
template <typename G_t>
void induced_subgraph_omit_edges(G_t &H, G_t &G,
                      typename std::set<typename boost::graph_traits<G_t>::vertex_descriptor> &X,
                      std::vector<std::vector<typename boost::graph_traits<G_t>::vertex_descriptor> > &edges,
                      typename std::vector<typename boost::graph_traits<G_t>::vertex_descriptor> &vdMap)
{
    std::vector<typename boost::graph_traits<G_t>::vertex_descriptor> internal_map(boost::num_vertices(G));
    std::vector<bool> disabled(boost::num_vertices(G), true);
    vdMap.resize(X.size());

    for(typename std::set<typename boost::graph_traits<G_t>::vertex_descriptor>::iterator sIt
         = X.begin(); sIt != X.end(); sIt++)
    {
       unsigned int pos1 = get_pos(*sIt, G);
       internal_map[pos1] = boost::add_vertex(H);
       disabled[pos1] = false;

       unsigned int pos2 = get_pos(internal_map[pos1], H);
       vdMap[pos2] = *sIt;
    }

    typename boost::graph_traits<G_t>::edge_iterator eIt, eEnd;
    for(boost::tie(eIt, eEnd) = boost::edges(G); eIt != eEnd; eIt++){
        unsigned int spos=get_pos(boost::source(*eIt, G), G);
        unsigned int dpos=get_pos(boost::target(*eIt, G), G);
        if(!disabled[spos] && !disabled[dpos]){
            bool omit = false;
            for(unsigned int i = 0; i < edges.size(); i++){
                if((edges[i][0] == boost::source(*eIt, G) && edges[i][1] == boost::target(*eIt, G))
                || (edges[i][1] == boost::source(*eIt, G) && edges[i][0] == boost::target(*eIt, G)))
                {
                    omit = true;
                    break;
                }
            }
            if(!omit){
                boost::add_edge(internal_map[spos], internal_map[dpos], H);
            }
        }
    }
}

// todo: prototype in graph.hpp
template <typename H_t, typename G_t, class S_t, class M_t>
void copy_induced_subgraph(H_t &H, G_t const &G, S_t const& X, M_t* vdMap)
{
    assert(boost::num_vertices(H)==0);
    typedef typename boost::graph_traits<G_t>::vertex_descriptor G_vertex_descriptor;
    typedef typename boost::graph_traits<H_t>::vertex_iterator H_vertex_iterator;
    std::vector<G_vertex_descriptor> internal_map(boost::num_vertices(G));
    std::vector<bool> disabled(boost::num_vertices(G), true);
    if(vdMap){
        vdMap->resize(X.size());
    }
    H = MOVE(G_t(X.size()));
    H_vertex_iterator h=boost::vertices(H).first;
    size_t pos2=0;

    for(typename S_t::const_iterator sIt=X.begin(); sIt!=X.end(); ++sIt){
       unsigned int pos1 = get_pos(*sIt, G);
       internal_map[pos1] = *h;
       ++h;
       disabled[pos1] = false;

       if(vdMap){
           (*vdMap)[pos2] = *sIt;
           ++pos2;
       }
    }
    assert(h==boost::vertices(H).second);

    typename boost::graph_traits<G_t>::edge_iterator eIt, eEnd;
    for(boost::tie(eIt, eEnd) = boost::edges(G); eIt!=eEnd; ++eIt){
        unsigned int spos=get_pos(boost::source(*eIt, G), G);
        unsigned int dpos=get_pos(boost::target(*eIt, G), G);
        if(!disabled[spos] && !disabled[dpos]){
            boost::add_edge(internal_map[spos], internal_map[dpos], H);
        }
    }
}

// paste subgraph of G induced by X into H.
// store map V(H) -> X \subset V(G) in vdMap.
//
// FIXME: misleading name. paste_induced_subgraph?
template <typename G_t, class S_t, class M_t>
void induced_subgraph(G_t &H, G_t const &G, S_t const& X, M_t* vdMap)
{
    if(boost::num_vertices(H)==0){
        return copy_induced_subgraph(H, G, X, vdMap);
    }
    std::vector<typename boost::graph_traits<G_t>::vertex_descriptor> internal_map(boost::num_vertices(G));
    std::vector<bool> disabled(boost::num_vertices(G), true);
    if(vdMap){
        vdMap->resize(X.size());
    }

    for(typename S_t::const_iterator sIt=X.begin(); sIt!=X.end(); ++sIt){
       unsigned int pos1 = get_pos(*sIt, G);
       internal_map[pos1] = boost::add_vertex(H);
       disabled[pos1] = false;

       if(vdMap){
           unsigned int pos2 = get_pos(internal_map[pos1], H);
           (*vdMap)[pos2] = *sIt;
       }
    }

    typename boost::graph_traits<G_t>::edge_iterator eIt, eEnd;
    for(boost::tie(eIt, eEnd) = boost::edges(G); eIt!=eEnd; ++eIt){
        unsigned int spos=get_pos(boost::source(*eIt, G), G);
        unsigned int dpos=get_pos(boost::target(*eIt, G), G);
        if(!disabled[spos] && !disabled[dpos]){
            boost::add_edge(internal_map[spos], internal_map[dpos], H);
        }
    }
}

template <typename G_t, class S_t, class M_t>
void induced_subgraph(G_t &H, G_t const &G, S_t const& X, M_t& vdMap)
{
    return induced_subgraph(H, G, X, &vdMap);
}

// same, but without vdMap
template <typename G_t, class S_t, class M_t>
void induced_subgraph(G_t &H, G_t const &G, S_t const& X)
{
    return induced_subgraph(H, G, X, NULL);
}

template <typename G_t>
bool is_edge_between_sets(G_t const &G,
                 typename std::set<typename boost::graph_traits<G_t>::vertex_descriptor> &X,
                 typename std::set<typename boost::graph_traits<G_t>::vertex_descriptor> &Y)
{
    for(typename std::set<typename boost::graph_traits<G_t>::vertex_descriptor>::iterator sIt1 = X.begin(); sIt1 != X.end(); sIt1++){
        for(typename std::set<typename boost::graph_traits<G_t>::vertex_descriptor>::iterator sIt2 = Y.begin(); sIt2 != Y.end(); sIt2++){
            if(boost::edge(*sIt1, *sIt2, G).second){
                return true;
            }
        }
    }
    return false;
}

template <typename G_t>
void get_neighbourhood(G_t const &G, std::vector<bool> &disabled,
             std::set<typename boost::graph_traits<G_t>::vertex_descriptor> &X,
             std::set<typename boost::graph_traits<G_t>::vertex_descriptor> &S_X)
{
    for(typename std::set<typename boost::graph_traits<G_t>::vertex_descriptor>::iterator sIt = X.begin(); sIt != X.end(); sIt++){
        typename boost::graph_traits<G_t>::adjacency_iterator nIt, nEnd;
        for(boost::tie(nIt, nEnd) = boost::adjacent_vertices(*sIt, G); nIt != nEnd; nIt++){
           unsigned int pos = get_pos(*nIt, G);
           if(!disabled[pos] && X.find(*nIt) == X.end()){
               S_X.insert(*nIt);
           }
        }
    }
}

template <typename G_t>
void t_search_components(G_t const &G,
        typename boost::graph_traits<G_t>::vertex_descriptor vertex,
        std::vector<bool> &visited,
        std::vector<std::set<typename boost::graph_traits<G_t>::vertex_descriptor> > &components,
        int comp_idx)
{
    unsigned int pos = get_pos(vertex, G);
    visited[pos] = true;
    typename boost::graph_traits<G_t>::adjacency_iterator  nIt, nEnd;
    for(boost::tie(nIt, nEnd) = boost::adjacent_vertices(vertex, G); nIt != nEnd; nIt++){
        unsigned int npos = get_pos(*nIt, G);
        if(!visited[npos]){
            components[comp_idx].insert(*nIt);
            t_search_components(G, *nIt, visited, components, comp_idx);
        }
    }
}


template <typename G_t>
void get_components_provided_map(G_t const &G,
             std::vector<std::set<typename boost::graph_traits<G_t>::vertex_descriptor> > &components,
             std::vector<bool> &visited){

    typename boost::graph_traits<G_t>::vertex_iterator vIt, vEnd;
    int comp_idx = -1;
    for(boost::tie(vIt, vEnd) = boost::vertices(G); vIt != vEnd; vIt++){
        unsigned int pos = get_pos(*vIt, G);
        if(!visited[pos]){
            components.resize(components.size()+1);
            comp_idx++;

            components[comp_idx].insert(*vIt);
            t_search_components(G, *vIt, visited, components, comp_idx);
        }
    }
}

template <typename G_t>
void t_search_components(G_t &G,
        typename boost::graph_traits<G_t>::vertex_descriptor vertex,
        std::vector<bool> &visited,
        std::vector<typename treedec_traits<typename treedec_chooser<G_t>::type>::bag_type> &components,
        int comp_idx)
{
    unsigned int pos = get_pos(vertex, G);
    visited[pos] = true;
    typename boost::graph_traits<G_t>::adjacency_iterator  nIt, nEnd;
    for(boost::tie(nIt, nEnd) = boost::adjacent_vertices(vertex, G); nIt != nEnd; nIt++){
        unsigned int npos = get_pos(*nIt, G);
        if(!visited[npos]){
            components[comp_idx].insert(*nIt);
            t_search_components(G, *nIt, visited, components, comp_idx);
        }
    }
}

template <typename G_t>
void get_components_provided_map(G_t &G,
             std::vector<typename treedec_traits<typename treedec_chooser<G_t>::type>::bag_type> &components,
             std::vector<bool> &visited){

    typename boost::graph_traits<G_t>::vertex_iterator vIt, vEnd;
    int comp_idx = -1;
    for(boost::tie(vIt, vEnd) = boost::vertices(G); vIt != vEnd; vIt++){
        unsigned int pos = get_pos(*vIt, G);
        if(!visited[pos]){
            components.resize(components.size()+1);
            comp_idx++;

            components[comp_idx].insert(*vIt);
            t_search_components(G, *vIt, visited, components, comp_idx);
        }
    }
}

template <typename G_t>
void get_components(G_t &G,
             std::vector<std::set<typename boost::graph_traits<G_t>::vertex_descriptor> > &components)
{
    std::vector<bool> visited(boost::num_vertices(G), false);
    typename boost::graph_traits<G_t>::vertex_iterator vIt, vEnd;
    int comp_idx = -1;
    for(boost::tie(vIt, vEnd) = boost::vertices(G); vIt != vEnd; vIt++){
        unsigned int pos = get_pos(*vIt, G);
        if(!visited[pos]){
            components.resize(components.size()+1);
            comp_idx++;

            components[comp_idx].insert(*vIt);
            t_search_components(G, *vIt, visited, components, comp_idx);
        }
    }
}

template <typename G_t>
inline typename boost::graph_traits<G_t>::vertex_descriptor
   get_least_common_vertex(const typename boost::graph_traits<G_t>::vertex_descriptor &min_vertex,
           const G_t &G)
{itested();
    typename boost::graph_traits<G_t>::adjacency_iterator nIt1, nIt2, nEnd;
    boost::tie(nIt1, nEnd) = boost::adjacent_vertices(min_vertex, G);
    typename boost::graph_traits<G_t>::vertex_descriptor w = *nIt1;

    unsigned int min_common = UINT_MAX;

    for(; nIt1 != nEnd; nIt1++){itested();
        unsigned int cnt_common = 0;
        BOOST_AUTO(ci, common_out_edges(*nIt1, min_vertex, G).first);
        BOOST_AUTO(ce, common_out_edges(*nIt1, min_vertex, G).second);
        for(; ci!=ce; ++ci){
            cnt_common++;
        }
        if(cnt_common < min_common){
            w = *nIt1;
            min_common = cnt_common;
        }
    }

    return w;
}

} //namespace treedec

#endif //TD_SIMPLE_GRAPH_ALGOS

// vim:ts=8:sw=4:et
