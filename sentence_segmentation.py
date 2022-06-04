# import spacy library
import spacy


from awt_pj import import_api

from py2neo import Graph

from awt_pj.import_api import uri, user, pwd

nlp = spacy.load("de_core_news_md")

courseGraph = Graph(uri, user=user, password=pwd)

courseIDs = courseGraph.run('MATCH (a:Course) RETURN a.Name, a.cid, a.descr')


# docu = "Im Kurs erlernen Sie den sicheren Umgang mit ihrer digitalen Kamera/Tablet/Handy, um in den verschiedensten Situationen die richtige Kameraeinstellung selbständig vornehmen zu können. "
text1 = "gesprochenes Deutsch verstehen"
text2 = "Im Kurs erlernen Sie den sicheren Umgang mit ihrer digitalen Kamera/Tablet/Handy, um in den verschiedensten Situationen die richtige Kameraeinstellung selbständig vornehmen zu können. Außerdem werden Grundkenntnisse in der Bildbearbeitung und Archivierung sowie das Aufbereiten der Fotos erlernt und vertieft. Das Ziel sind anwendungsbereite Kenntnisse sowie Fähigkeiten der Bildaufnahme und -bearbeitung. Der Kurs ist geeignet für Personen, die im Berufsalltag zur Dokumentation von Ergebnissen/Arbeiten/Schäden die Fotografie nutzen. Ausführliche Info auf der Webseite.  "
nlp.add_pipe("merge_noun_chunks")
nlp.add_pipe("merge_entities")
doc = nlp(text2)
# print([t.lemma_ for t in doc ])
for sent in doc.sents:
    print(sent.text)
    print([t.text for t in sent])
    print("\n")

# for name, id, descr in courseIDs:
#   # descr = courseGraph.run('MATCH (a:Course) RETURN a.descr')
#     if name == "Fotografie Basiswissen Dokumentation in Beruf u. Alltag/Bildungsfreistellung":
#         nlp.add_pipe("merge_noun_chunks")
#         nlp.add_pipe("merge_entities")
#         # nlp.add_pipe("merge_subtokens")
#         doc = nlp(descr)
#         print(nlp.pipe_names)
#         print(name)
# #         sentence segmentation
#         for sent in doc.sents:
#             print(sent.text)
#             print([t.text for t in sent])
#             print("\n")
#             # break
#         # sentsList = list(doc.sents)
#
# #         tokenize
#         # tokenList = list(doc)
#         # print("length of tokenlist: ", len(tokenList))
#         # break
#         # print("____________\n")
#
# #         Part of Speech
# #         all_tags = [{w.pos:w.pos_ for w in sent} for sent in list(doc.sents) ]
#
#         # for sent in list(doc.sents):
#         #     for word in sent:
#         #         print(word, word.tag_)
#
# #       noun phrases
# #         for np in doc.noun_chunks:
# #             print(np.text, np.root.dep_, np.root.head.text)
# #             print(np.text)
#         break
