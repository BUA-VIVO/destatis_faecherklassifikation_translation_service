# -*- coding: utf-8 -*-
import json

from functions.translator import RDFTranslator


# Do initial automatic translation over the Goodle Translate API
# rdftranslator = RDFTranslator('../faecherklassifikation.rdf', 'de', 'en')
# skosgraph = rdftranslator.processrdf()
# #
# print("Serializing graph to XMl/RDF")
# with open('../faecherklassifikation_en_manual.rdf', 'w') as file_object:
#     file_object.write(skosgraph.serialize(format='xml'))
#
# print("Serializing graph to turtle format")
# with open('../faecherklassifikation_en_manual.ttl', 'w') as file_object:
#     file_object.write(skosgraph.serialize())
#
# print("Serializing graph to n3 format")
# with open('../faecherklassifikation_en_manual.ttl', 'w') as file_object:
#     file_object.write(skosgraph.serialize(format="n3"))


# If needed, Capitalize Literals after manual Proof reading

# rdfcapitalizer = RDFTranslator('../faecherklassifikation_en_manual.ttl', 'de', 'en')
# names = rdfcapitalizer.capitalizenames('en')
#
# print("Serializing capitalized graph to turtle format")
# with open('../faecherklassifikation_en_orig.ttl', 'w') as file_object:
#     file_object.write(names.serialize())
#
# print("Serializing graph to XMl/RDF")
# with open('../faecherklassifikation_en.rdf', 'w') as file_object:
#     file_object.write(names.serialize(format='xml'))
#
# print("Serializing graph to n3 format")
# with open('../faecherklassifikation_en.n3', 'w') as file_object:
#     file_object.write(names.serialize(format="n3"))

triplecherrypicker = RDFTranslator('../faecherklassifikation_en_orig.ttl', 'de', 'en')
cherrypicked = triplecherrypicker.cherrypicktriples({"https://onto.tib.eu/destf/cs": "*", "http://www.w3.org/2004/02/skos/core#prefLabel": "en-US", "http://www.w3.org/2000/01/rdf-schema#label": ["en-US", "de-DE"]})
print("Serializing cherrypicked graph to turtle format")
with open('../faecherklassifikation_en.ttl', 'w') as file_object:
    file_object.write(cherrypicked.serialize())

print("Serializing cherrypicked to XMl/RDF")
with open('../faecherklassifikation_en.rdf', 'w') as file_object:
    file_object.write(cherrypicked.serialize(format='xml'))

print("Serializing cherrypicked to n3 format")
with open('../faecherklassifikation_en.n3', 'w') as file_object:
    file_object.write(cherrypicked.serialize(format="n3"))
