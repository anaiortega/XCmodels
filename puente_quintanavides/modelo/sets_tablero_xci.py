\mdlr
    \sets
       {
         \def_set["setVoladizoIzquierdo"]{sel_faces_lista(tagsCarasVoladizoIzquierdo) fillDownwards()}
         \def_set["setVoladizoDerecho"]{sel_faces_lista(tagsCarasVoladizoDerecho) fillDownwards()}

         \def_set["setLosaViaIzquierda"]{sel_faces_lista(tagsCarasLosaViaIzquierda) fillDownwards()}
         \def_set["setLosaViaDerecha"]{sel_faces_lista(tagsCarasLosaViaDerecha) fillDownwards()}

         \def_set["setVoladizos"]{sel_set("setVoladizoIzquierdo") sel_set("setVoladizoDerecho")}
         \def_set["setLosasVias"]{sel_set("setLosaViaIzquierda") sel_set("setLosaViaDerecha")}
         \def_set["setLosaSup"]{sel_set("setVoladizos") sel_set("setLosasVias")}

         \def_set["setAlmaIzquierda"]{sel_faces_lista(tagsCarasAlmaIzquierda) fillDownwards() }
         \def_set["setAlmaCentral"]{sel_faces_lista(tagsCarasAlmaCentral) fillDownwards() }
         \def_set["setAlmaDerecha"]{sel_faces_lista(tagsCarasAlmaDerecha) fillDownwards() }
         \def_set["setAlmasLaterales"]{sel_set("setAlmaIzquierda") sel_set("setAlmaDerecha")}
         \def_set["setAlmas"]{sel_set("setAlmasLaterales") sel_set("setAlmaCentral")}

         \def_set["setLosaInfIzquierda"]{sel_faces_lista(tagsCarasLosaInfIzquierda) fillDownwards() }
         \def_set["setLosaInfDerecha"]{sel_faces_lista(tagsCarasLosaInfDerecha) fillDownwards() }
         \def_set["setLosaInf"]{sel_set("setLosaInfIzquierda") sel_set("setLosaInfDerecha")}

         \def_set["setArtesa"]{sel_set("setLosaInf") sel_set("setAlmas")}
         
         \def_set["setDiafragmaDorsal"]{sel_faces_lista(tagsCarasDiafragmaDorsal)  fillDownwards()}
         \def_set["setDiafragmaFrontal"]{sel_faces_lista(tagsCarasDiafragmaFrontal)  fillDownwards()}
         \def_set["setDiafragmas"]{sel_set("setDiafragmaDorsal") sel_set("setDiafragmaFrontal")}


         \def_set["setTramo0"]{sel_set_cond("total","hasLabel(idTramo0)") fillDownwards()}
         \def_set["setTramo1"]{sel_set_cond("total","hasLabel(idTramo1)") fillDownwards()}
         \def_set["setTramo2"]{sel_set_cond("total","hasLabel(idTramo2)") fillDownwards()}
         \def_set["setTramo3"]{sel_set_cond("total","hasLabel(idTramo3)") fillDownwards()}
         \def_set["setTramo4"]{sel_set_cond("total","hasLabel(idTramo4)") fillDownwards()}
         \def_set["setTramo5"]{sel_set_cond("total","hasLabel(idTramo5)") fillDownwards()}
         \def_set["setTramo6"]{sel_set_cond("total","hasLabel(idTramo6)") fillDownwards()}

         \def_set["setAlmas30"]
           {
             sel_set_cond("setAlmasLaterales","hasLabel(idTramo0)")
             sel_set_cond("setAlmasLaterales","hasLabel(idTramo1)")
             sel_set_cond("setAlmasLaterales","hasLabel(idTramo5)")
             sel_set_cond("setAlmasLaterales","hasLabel(idTramo6)")
             fillDownwards()
           }
         \def_set["setAlmas27"]
           {
             sel_set_cond("setAlmasLaterales","hasLabel(idTramo2)")
             sel_set_cond("setAlmasLaterales","hasLabel(idTramo4)")
             fillDownwards()
           }
         \def_set["setAlmas22"]
           {
             sel_set_cond("setAlmasLaterales","hasLabel(idTramo3)")
             fillDownwards()
           }

         \def_set["setAlmasC50"]
           {
             sel_set_cond("setAlmaCentral","hasLabel(idTramo1)")
             sel_set_cond("setAlmaCentral","hasLabel(idTramo5)")
             fillDownwards()
           }
         \def_set["setAlmasC40"]
           {
             sel_set_cond("setAlmaCentral","hasLabel(idTramo2)")
             sel_set_cond("setAlmaCentral","hasLabel(idTramo3)")
             sel_set_cond("setAlmaCentral","hasLabel(idTramo4)")
             fillDownwards()
           }

       }
  }
