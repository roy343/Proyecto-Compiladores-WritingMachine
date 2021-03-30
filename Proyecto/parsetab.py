
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'A AA AF ALEATORIO COMA CUANDO DAA DAB DCL DEC DEFAULT DESDE DFA DFB DIFERENTE DOSPUNTOS ENCASO ENTONS F FIN FINDESDE FINENCASO FINPROC HAGA HASTA HASTAENCONTRAR IAA IAB ID IFA IFB IGUAL INC INI INICIO INICIOPROC LLAMAR LLAVE_DER LLAVE_IZQ MAYOR MAYORIGUAL MENOR MENORIGUAL MOVER NUMERO PARENTESIS_DER PARENTESIS_IZQ PROC PUNTOCOMA REPITA SINO SUMA\n    Start : code\n    \n    code : INICIO DOSPUNTOS cuerpo FIN PUNTOCOMA procedimiento\n    \n    cuerpo : variable\n            | expresion\n    \n    variable : variable1 cuerpo\n            | variable2 cuerpo\n            | empty empty\n    \n    variable1 : DCL ID PUNTOCOMA\n    \n    variable2 : DCL ID DEFAULT NUMERO PUNTOCOMA\n    \n    expresion : condicion1 expresion\n            | condicion2 expresion\n            | repita expresion\n            | hacer expresion\n            | funcion expresion\n            | llamarProc expresion\n            | empty empty\n    \n    condicion1 : ENCASO cond1Aux1 FINENCASO PUNTOCOMA\n    \n    cond1Aux1 : cond1Aux2 SINO LLAVE_IZQ expresion LLAVE_DER\n            | empty empty empty empty empty\n    \n    cond1Aux2 : CUANDO ID condicion sentencia ENTONS LLAVE_IZQ expresion LLAVE_DER cond1Aux2\n            | empty empty empty empty empty empty empty empty empty\n    \n    condicion2 : ENCASO ID cond2Aux1 FINENCASO PUNTOCOMA\n    \n    cond2Aux1 : cond2Aux2 SINO LLAVE_IZQ expresion LLAVE_DER\n                | empty empty empty empty empty\n    \n        cond2Aux2 : CUANDO  condicion sentencia ENTONS LLAVE_IZQ expresion LLAVE_DER cond2Aux2\n                | empty empty empty empty empty empty empty empty\n        \n    condicion : IGUAL\n              | MAYOR\n              | MENOR\n              | DIFERENTE\n              | MAYORIGUAL\n              | MENORIGUAL\n    \n    sentencia : ID\n               | NUMERO\n    \n     repita : REPITA LLAVE_IZQ expresion LLAVE_DER HASTAENCONTRAR ID condicion sentencia PUNTOCOMA\n    \n    hacer : DESDE ID IGUAL sentencia HASTA sentencia HAGA LLAVE_IZQ expresion LLAVE_DER FINDESDE PUNTOCOMA\n    \n    funcion : Aleatorio\n            | Mover\n            | funcionAlge\n    \n    Aleatorio : ALEATORIO PARENTESIS_IZQ PARENTESIS_DER PUNTOCOMA\n    \n    Mover : MOVER PARENTESIS_IZQ paramMover PARENTESIS_DER PUNTOCOMA\n    \n    paramMover : AF\n                | F\n                | DFA\n                | IFA\n                | DFB\n                | IFB\n                | A\n                | DAA\n                | IAA\n                | DAB\n                | IAB\n                | AA\n    \n    funcionAlge : INC PARENTESIS_IZQ ID COMA sentencia PARENTESIS_DER PUNTOCOMA\n             | DEC PARENTESIS_IZQ ID COMA sentencia PARENTESIS_DER PUNTOCOMA\n             | INI PARENTESIS_IZQ ID COMA sentencia PARENTESIS_DER PUNTOCOMA\n    \n        procedimiento : PROC ID PARENTESIS_IZQ parametro PARENTESIS_DER INICIOPROC DOSPUNTOS expresion FINPROC PUNTOCOMA procedimiento\n                     | empty empty empty empty empty empty empty empty empty empty empty\n    \n    parametro : ID COMA parametro\n              | ID empty empty\n              | NUMERO COMA parametro\n              | NUMERO empty empty\n              | empty empty empty\n\n    \n    llamarProc : LLAMAR ID PARENTESIS_IZQ parametro PARENTESIS_DER PUNTOCOMA\n    \n    empty :\n    '
    
_lr_action_items = {'INICIO':([0,],[3,]),'$end':([1,2,55,87,89,119,141,160,172,180,188,197,202,206,207,210,211,],[0,-1,-65,-2,-65,-65,-65,-65,-65,-65,-65,-65,-65,-65,-65,-57,-58,]),'DOSPUNTOS':([3,179,],[4,187,]),'DCL':([4,8,9,57,120,],[17,17,17,-8,-9,]),'FIN':([4,5,6,7,8,9,10,11,12,13,14,15,16,21,22,23,31,32,33,34,35,36,37,38,39,40,56,57,91,113,120,121,136,152,168,169,170,185,205,],[-65,30,-3,-4,-65,-65,-65,-65,-65,-65,-65,-65,-65,-37,-38,-39,-5,-6,-7,-10,-65,-11,-12,-13,-14,-15,-16,-8,-17,-40,-9,-22,-41,-64,-54,-55,-56,-35,-36,]),'ENCASO':([4,8,9,11,12,13,14,15,16,21,22,23,47,57,91,102,113,120,121,122,136,152,163,165,168,169,170,178,185,187,205,],[18,18,18,18,18,18,18,18,18,-37,-38,-39,18,-8,-17,18,-40,-9,-22,18,-41,-64,18,18,-54,-55,-56,18,-35,18,-36,]),'REPITA':([4,8,9,11,12,13,14,15,16,21,22,23,47,57,91,102,113,120,121,122,136,152,163,165,168,169,170,178,185,187,205,],[19,19,19,19,19,19,19,19,19,-37,-38,-39,19,-8,-17,19,-40,-9,-22,19,-41,-64,19,19,-54,-55,-56,19,-35,19,-36,]),'DESDE':([4,8,9,11,12,13,14,15,16,21,22,23,47,57,91,102,113,120,121,122,136,152,163,165,168,169,170,178,185,187,205,],[20,20,20,20,20,20,20,20,20,-37,-38,-39,20,-8,-17,20,-40,-9,-22,20,-41,-64,20,20,-54,-55,-56,20,-35,20,-36,]),'LLAMAR':([4,8,9,11,12,13,14,15,16,21,22,23,47,57,91,102,113,120,121,122,136,152,163,165,168,169,170,178,185,187,205,],[24,24,24,24,24,24,24,24,24,-37,-38,-39,24,-8,-17,24,-40,-9,-22,24,-41,-64,24,24,-54,-55,-56,24,-35,24,-36,]),'ALEATORIO':([4,8,9,11,12,13,14,15,16,21,22,23,47,57,91,102,113,120,121,122,136,152,163,165,168,169,170,178,185,187,205,],[25,25,25,25,25,25,25,25,25,-37,-38,-39,25,-8,-17,25,-40,-9,-22,25,-41,-64,25,25,-54,-55,-56,25,-35,25,-36,]),'MOVER':([4,8,9,11,12,13,14,15,16,21,22,23,47,57,91,102,113,120,121,122,136,152,163,165,168,169,170,178,185,187,205,],[26,26,26,26,26,26,26,26,26,-37,-38,-39,26,-8,-17,26,-40,-9,-22,26,-41,-64,26,26,-54,-55,-56,26,-35,26,-36,]),'INC':([4,8,9,11,12,13,14,15,16,21,22,23,47,57,91,102,113,120,121,122,136,152,163,165,168,169,170,178,185,187,205,],[27,27,27,27,27,27,27,27,27,-37,-38,-39,27,-8,-17,27,-40,-9,-22,27,-41,-64,27,27,-54,-55,-56,27,-35,27,-36,]),'DEC':([4,8,9,11,12,13,14,15,16,21,22,23,47,57,91,102,113,120,121,122,136,152,163,165,168,169,170,178,185,187,205,],[28,28,28,28,28,28,28,28,28,-37,-38,-39,28,-8,-17,28,-40,-9,-22,28,-41,-64,28,28,-54,-55,-56,28,-35,28,-36,]),'INI':([4,8,9,11,12,13,14,15,16,21,22,23,47,57,91,102,113,120,121,122,136,152,163,165,168,169,170,178,185,187,205,],[29,29,29,29,29,29,29,29,29,-37,-38,-39,29,-8,-17,29,-40,-9,-22,29,-41,-64,29,29,-54,-55,-56,29,-35,29,-36,]),'LLAVE_DER':([11,12,13,14,15,16,21,22,23,34,35,36,37,38,39,40,47,56,67,91,102,113,121,122,125,136,142,152,163,165,168,169,170,174,176,178,185,186,205,],[-65,-65,-65,-65,-65,-65,-37,-38,-39,-10,-65,-11,-12,-13,-14,-15,-65,-16,105,-17,-65,-40,-22,-65,145,-41,161,-64,-65,-65,-54,-55,-56,182,184,-65,-35,195,-36,]),'FINPROC':([11,12,13,14,15,16,21,22,23,34,35,36,37,38,39,40,56,91,113,121,136,152,168,169,170,185,187,196,205,],[-65,-65,-65,-65,-65,-65,-37,-38,-39,-10,-65,-11,-12,-13,-14,-15,-16,-17,-40,-22,-41,-64,-54,-55,-56,-35,-65,201,-36,]),'ID':([17,18,20,24,46,52,53,54,68,69,88,95,96,97,98,99,100,101,104,115,116,117,128,129,130,134,140,166,],[41,43,48,49,66,84,85,86,106,109,118,106,-27,-28,-29,-30,-31,-32,106,106,106,106,148,106,109,109,109,106,]),'CUANDO':([18,43,182,184,],[46,63,63,46,]),'FINENCASO':([18,42,43,45,60,62,65,94,103,123,126,143,145,146,161,162,],[-65,59,-65,-65,92,-65,-65,-65,-65,-65,-65,-65,-18,-19,-23,-24,]),'SINO':([18,43,44,45,61,62,65,94,103,123,126,143,146,162,164,173,175,181,182,183,184,189,190,191,192,193,194,198,199,203,204,208,209,212,213,],[-65,-65,64,-65,93,-65,-65,-65,-65,-65,-65,-65,-65,-65,-65,-65,-65,-65,-65,-65,-65,-26,-25,-65,-21,-20,-65,-65,-65,-65,-65,-65,-65,-65,-65,]),'LLAVE_IZQ':([19,64,93,144,147,167,],[47,102,122,163,165,178,]),'PARENTESIS_IZQ':([25,26,27,28,29,49,118,],[50,51,52,53,54,69,140,]),'PUNTOCOMA':([30,41,59,70,90,92,106,108,114,132,156,157,158,177,200,201,],[55,57,91,113,120,121,-33,-34,136,152,168,169,170,185,205,206,]),'DEFAULT':([41,],[58,]),'IGUAL':([48,63,66,148,],[68,96,96,96,]),'PARENTESIS_DER':([50,69,71,72,73,74,75,76,77,78,79,80,81,82,83,106,108,109,110,111,112,130,131,133,134,135,137,138,139,140,150,151,153,154,155,159,],[70,-65,114,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-33,-34,-65,132,-65,-65,-65,-65,-65,-65,-65,156,157,158,-65,-59,-60,-63,-61,-62,171,]),'AF':([51,],[72,]),'F':([51,],[73,]),'DFA':([51,],[74,]),'IFA':([51,],[75,]),'DFB':([51,],[76,]),'IFB':([51,],[77,]),'A':([51,],[78,]),'DAA':([51,],[79,]),'IAA':([51,],[80,]),'DAB':([51,],[81,]),'IAB':([51,],[82,]),'AA':([51,],[83,]),'PROC':([55,206,],[88,88,]),'NUMERO':([58,68,69,95,96,97,98,99,100,101,104,115,116,117,129,130,134,140,166,],[90,108,112,108,-27,-28,-29,-30,-31,-32,108,108,108,108,108,112,112,112,108,]),'MAYOR':([63,66,148,],[97,97,97,]),'MENOR':([63,66,148,],[98,98,98,]),'DIFERENTE':([63,66,148,],[99,99,99,]),'MAYORIGUAL':([63,66,148,],[100,100,100,]),'MENORIGUAL':([63,66,148,],[101,101,101,]),'COMA':([84,85,86,109,112,],[115,116,117,130,134,]),'HASTAENCONTRAR':([105,],[128,]),'HASTA':([106,107,108,],[-33,129,-34,]),'ENTONS':([106,108,124,127,],[-33,-34,144,147,]),'HAGA':([106,108,149,],[-33,-34,167,]),'INICIOPROC':([171,],[179,]),'FINDESDE':([195,],[200,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Start':([0,],[1,]),'code':([0,],[2,]),'cuerpo':([4,8,9,],[5,31,32,]),'variable':([4,8,9,],[6,6,6,]),'expresion':([4,8,9,11,12,13,14,15,16,47,102,122,163,165,178,187,],[7,7,7,34,36,37,38,39,40,67,125,142,174,176,186,196,]),'variable1':([4,8,9,],[8,8,8,]),'variable2':([4,8,9,],[9,9,9,]),'empty':([4,8,9,10,11,12,13,14,15,16,18,35,43,45,47,55,62,65,69,89,94,102,103,109,111,112,119,122,123,126,130,131,133,134,135,140,141,143,146,160,162,163,164,165,172,173,175,178,180,181,182,183,184,187,188,191,194,197,198,199,202,203,204,206,207,208,209,212,213,],[10,10,10,33,35,35,35,35,35,35,45,56,62,65,35,89,94,103,111,119,123,35,126,131,133,135,141,35,143,146,111,151,153,111,155,111,160,162,164,172,173,35,175,35,180,181,183,35,188,189,191,192,194,35,197,198,199,202,203,204,207,208,209,89,211,212,213,173,164,]),'condicion1':([4,8,9,11,12,13,14,15,16,47,102,122,163,165,178,187,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'condicion2':([4,8,9,11,12,13,14,15,16,47,102,122,163,165,178,187,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'repita':([4,8,9,11,12,13,14,15,16,47,102,122,163,165,178,187,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'hacer':([4,8,9,11,12,13,14,15,16,47,102,122,163,165,178,187,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'funcion':([4,8,9,11,12,13,14,15,16,47,102,122,163,165,178,187,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'llamarProc':([4,8,9,11,12,13,14,15,16,47,102,122,163,165,178,187,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'Aleatorio':([4,8,9,11,12,13,14,15,16,47,102,122,163,165,178,187,],[21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'Mover':([4,8,9,11,12,13,14,15,16,47,102,122,163,165,178,187,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'funcionAlge':([4,8,9,11,12,13,14,15,16,47,102,122,163,165,178,187,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'cond1Aux1':([18,],[42,]),'cond1Aux2':([18,184,],[44,193,]),'cond2Aux1':([43,],[60,]),'cond2Aux2':([43,182,],[61,190,]),'paramMover':([51,],[71,]),'procedimiento':([55,206,],[87,210,]),'condicion':([63,66,148,],[95,104,166,]),'sentencia':([68,95,104,115,116,117,129,166,],[107,124,127,137,138,139,149,177,]),'parametro':([69,130,134,140,],[110,150,154,159,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Start","S'",1,None,None,None),
  ('Start -> code','Start',1,'p_Start','IDE.py',14),
  ('code -> INICIO DOSPUNTOS cuerpo FIN PUNTOCOMA procedimiento','code',6,'p_Code','IDE.py',21),
  ('cuerpo -> variable','cuerpo',1,'p_cuerpo','IDE.py',29),
  ('cuerpo -> expresion','cuerpo',1,'p_cuerpo','IDE.py',30),
  ('variable -> variable1 cuerpo','variable',2,'p_Variable','IDE.py',37),
  ('variable -> variable2 cuerpo','variable',2,'p_Variable','IDE.py',38),
  ('variable -> empty empty','variable',2,'p_Variable','IDE.py',39),
  ('variable1 -> DCL ID PUNTOCOMA','variable1',3,'p_Variable1','IDE.py',50),
  ('variable2 -> DCL ID DEFAULT NUMERO PUNTOCOMA','variable2',5,'p_Variable2','IDE.py',57),
  ('expresion -> condicion1 expresion','expresion',2,'p_expresion','IDE.py',64),
  ('expresion -> condicion2 expresion','expresion',2,'p_expresion','IDE.py',65),
  ('expresion -> repita expresion','expresion',2,'p_expresion','IDE.py',66),
  ('expresion -> hacer expresion','expresion',2,'p_expresion','IDE.py',67),
  ('expresion -> funcion expresion','expresion',2,'p_expresion','IDE.py',68),
  ('expresion -> llamarProc expresion','expresion',2,'p_expresion','IDE.py',69),
  ('expresion -> empty empty','expresion',2,'p_expresion','IDE.py',70),
  ('condicion1 -> ENCASO cond1Aux1 FINENCASO PUNTOCOMA','condicion1',4,'p_condicion1','IDE.py',80),
  ('cond1Aux1 -> cond1Aux2 SINO LLAVE_IZQ expresion LLAVE_DER','cond1Aux1',5,'p_cond1Aux1','IDE.py',87),
  ('cond1Aux1 -> empty empty empty empty empty','cond1Aux1',5,'p_cond1Aux1','IDE.py',88),
  ('cond1Aux2 -> CUANDO ID condicion sentencia ENTONS LLAVE_IZQ expresion LLAVE_DER cond1Aux2','cond1Aux2',9,'p_cond1Aux2','IDE.py',98),
  ('cond1Aux2 -> empty empty empty empty empty empty empty empty empty','cond1Aux2',9,'p_cond1Aux2','IDE.py',99),
  ('condicion2 -> ENCASO ID cond2Aux1 FINENCASO PUNTOCOMA','condicion2',5,'p_condicion2','IDE.py',111),
  ('cond2Aux1 -> cond2Aux2 SINO LLAVE_IZQ expresion LLAVE_DER','cond2Aux1',5,'p_cond2Aux1','IDE.py',118),
  ('cond2Aux1 -> empty empty empty empty empty','cond2Aux1',5,'p_cond2Aux1','IDE.py',119),
  ('cond2Aux2 -> CUANDO condicion sentencia ENTONS LLAVE_IZQ expresion LLAVE_DER cond2Aux2','cond2Aux2',8,'p_cond2Aux2','IDE.py',129),
  ('cond2Aux2 -> empty empty empty empty empty empty empty empty','cond2Aux2',8,'p_cond2Aux2','IDE.py',130),
  ('condicion -> IGUAL','condicion',1,'p_condicion','IDE.py',142),
  ('condicion -> MAYOR','condicion',1,'p_condicion','IDE.py',143),
  ('condicion -> MENOR','condicion',1,'p_condicion','IDE.py',144),
  ('condicion -> DIFERENTE','condicion',1,'p_condicion','IDE.py',145),
  ('condicion -> MAYORIGUAL','condicion',1,'p_condicion','IDE.py',146),
  ('condicion -> MENORIGUAL','condicion',1,'p_condicion','IDE.py',147),
  ('sentencia -> ID','sentencia',1,'p_sentencia','IDE.py',155),
  ('sentencia -> NUMERO','sentencia',1,'p_sentencia','IDE.py',156),
  ('repita -> REPITA LLAVE_IZQ expresion LLAVE_DER HASTAENCONTRAR ID condicion sentencia PUNTOCOMA','repita',9,'p_repita','IDE.py',163),
  ('hacer -> DESDE ID IGUAL sentencia HASTA sentencia HAGA LLAVE_IZQ expresion LLAVE_DER FINDESDE PUNTOCOMA','hacer',12,'p_hacer','IDE.py',170),
  ('funcion -> Aleatorio','funcion',1,'p_funcion','IDE.py',177),
  ('funcion -> Mover','funcion',1,'p_funcion','IDE.py',178),
  ('funcion -> funcionAlge','funcion',1,'p_funcion','IDE.py',179),
  ('Aleatorio -> ALEATORIO PARENTESIS_IZQ PARENTESIS_DER PUNTOCOMA','Aleatorio',4,'p_aleatorio','IDE.py',186),
  ('Mover -> MOVER PARENTESIS_IZQ paramMover PARENTESIS_DER PUNTOCOMA','Mover',5,'p_mover','IDE.py',193),
  ('paramMover -> AF','paramMover',1,'p_ParamMover','IDE.py',200),
  ('paramMover -> F','paramMover',1,'p_ParamMover','IDE.py',201),
  ('paramMover -> DFA','paramMover',1,'p_ParamMover','IDE.py',202),
  ('paramMover -> IFA','paramMover',1,'p_ParamMover','IDE.py',203),
  ('paramMover -> DFB','paramMover',1,'p_ParamMover','IDE.py',204),
  ('paramMover -> IFB','paramMover',1,'p_ParamMover','IDE.py',205),
  ('paramMover -> A','paramMover',1,'p_ParamMover','IDE.py',206),
  ('paramMover -> DAA','paramMover',1,'p_ParamMover','IDE.py',207),
  ('paramMover -> IAA','paramMover',1,'p_ParamMover','IDE.py',208),
  ('paramMover -> DAB','paramMover',1,'p_ParamMover','IDE.py',209),
  ('paramMover -> IAB','paramMover',1,'p_ParamMover','IDE.py',210),
  ('paramMover -> AA','paramMover',1,'p_ParamMover','IDE.py',211),
  ('funcionAlge -> INC PARENTESIS_IZQ ID COMA sentencia PARENTESIS_DER PUNTOCOMA','funcionAlge',7,'p_funcion_Alge','IDE.py',218),
  ('funcionAlge -> DEC PARENTESIS_IZQ ID COMA sentencia PARENTESIS_DER PUNTOCOMA','funcionAlge',7,'p_funcion_Alge','IDE.py',219),
  ('funcionAlge -> INI PARENTESIS_IZQ ID COMA sentencia PARENTESIS_DER PUNTOCOMA','funcionAlge',7,'p_funcion_Alge','IDE.py',220),
  ('procedimiento -> PROC ID PARENTESIS_IZQ parametro PARENTESIS_DER INICIOPROC DOSPUNTOS expresion FINPROC PUNTOCOMA procedimiento','procedimiento',11,'p_procedimiento','IDE.py',228),
  ('procedimiento -> empty empty empty empty empty empty empty empty empty empty empty','procedimiento',11,'p_procedimiento','IDE.py',229),
  ('parametro -> ID COMA parametro','parametro',3,'p_parametro','IDE.py',241),
  ('parametro -> ID empty empty','parametro',3,'p_parametro','IDE.py',242),
  ('parametro -> NUMERO COMA parametro','parametro',3,'p_parametro','IDE.py',243),
  ('parametro -> NUMERO empty empty','parametro',3,'p_parametro','IDE.py',244),
  ('parametro -> empty empty empty','parametro',3,'p_parametro','IDE.py',245),
  ('llamarProc -> LLAMAR ID PARENTESIS_IZQ parametro PARENTESIS_DER PUNTOCOMA','llamarProc',6,'p_llamarProc','IDE.py',256),
  ('empty -> <empty>','empty',0,'p_empty','IDE.py',263),
]
