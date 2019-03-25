from SPARQLWrapper import SPARQLWrapper, JSON
import traceback
from utlis.query_entity_number import query_entity
from utlis.add_tag_on_model import tag_model

model = tag_model('./origin_data/grammar', './deal_data/tag_model')
entity = query_entity('./deal_data/tag_model')
for i in entity:
    queryString = ('SELECT DISTINCT  ?cp_label ?dp_label' + '\n'
                   'WHERE {' + '\n'
                   'VALUES ?c_label{' + '"' + i + '"' + '}.' + '\n'
                   '{VALUES ?dp_type{<http://hual.ai/new_standard#BooleanProperty><http://hual.ai/new_standard#DateProperty><http://hual.ai/new_standard#EnumProperty>' + '\n'
                   '<http://hual.ai/new_standard#TextProperty><http://hual.ai/new_standard#DateProperty>}' + '\n'
                   '?s a ?class.' + '\n'
                   '?class rdfs:label ?c_label.' + '\n'
                   '?cp rdfs:domain ?cp_domain.' + '\n'
                   '?cp rdf:type <http://hual.ai/new_standard#ComplexProperty>.' + '\n'                                
                   '?class rdfs:subClassOf* ?cp_domain.' + '\n'
                   '?dp rdfs:domain ?dp_domain.' + '\n'
                   '?bn a ?bnclass.' + '\n'
                   '?bnclass rdf:type <http://hual.ai/new_standard#BNclass>.' + '\n'                   
                   '?bnclass rdfs:subClassOf* ?dp_domain.' + '\n'
                   '?cp rdfs:label ?cp_label.' + '\n'
                   '?dp rdfs:label ?dp_label.' + '\n'
                   '?dp rdf:type ?dp_type.}' + '\n'                             
                   'UNION' + '\n'
                   '{VALUES ?dp_type{<http://hual.ai/new_standard#BooleanProperty><http://hual.ai/new_standard#DateProperty><http://hual.ai/new_standard#EnumProperty>' + '\n'
                   '<http://hual.ai/new_standard#TextProperty><http://hual.ai/new_standard#ObjectProperty>}' + '\n'                                                                                                                                                       
                   '?s a ?class.' + '\n'
                   '?class rdfs:label ?c_label.' + '\n'
                   '?dp rdfs:domain ?dp_domain.' + '\n'
                   '?class rdfs:subClassOf* ?dp_domain.' + '\n'
                   '?dp rdfs:label ?dp_label.' + '\n'
                   '?dp rdf:type ?dp_type}}' + '\n'                               
                   'ORDER BY ?cp')
    sparql = SPARQLWrapper("http://115.182.62.171:8891/sparql")
    sparql.addDefaultGraph("http://localhost/labrador/taikang_rs_dev")
    sparql.setQuery(queryString)
    try:
        sparql.setReturnFormat(JSON)
        temp = sparql.query().convert()
        if len(temp['results']['bindings']) == 0:
            print(i + '\t' + '没有属性值')
        else:
            with open('./dict_cpdp/' + i, 'a', encoding='utf-8')as f:
                for j in temp['results']['bindings']:
                    if len(j) == 2:
                        f.write('cd' + '\t' + j['cp_label']['value'] + '\t' + j['dp_label']['value'] + '\n')
                    elif j['dp_label']['value'] is not None:
                        f.write('d' + '\t' * 2 + j['dp_label']['value'] + '\n')
                    elif j['cp_label']['value'] is not None:
                        f.write('c' + '\t' * 2 + j['cp_label']['value'] + '\n')
    except:
        traceback.print_exc()
