
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'A AA AF COMA DAA DAB DEC DEF DEFAULT DFA DFB DIFERENTE DOSPUNTOS END ENDIF F FIN IAA IAB ID IF IFA IFB IFELSE IGUAL INC INI LLAVE_DER LLAVE_IZQ MAYOR MAYORIGUAL MENOR MENORIGUAL MOVER NUMERO PARA PARENTESIS_DER PARENTESIS_IZQ PROC PUNTOCOMA RANDOM REPEAT RUN START SUMA THEN UNTIL WHILE\n    Start : code\n    \n    code : START DOSPUNTOS cuerpo END PUNTOCOMA procedimiento\n    \n    cuerpo : variable\n            | expresion\n    \n    variable : variable1 cuerpo\n            | variable2 cuerpo\n            | empty empty\n    \n    variable1 : DEF ID PUNTOCOMA\n    \n    variable2 : DEF ID DEFAULT NUMERO PUNTOCOMA\n    \n    expresion : condicion1 expresion\n            | condicion2 expresion\n            | repita expresion\n            | hacer expresion\n            | funcion expresion\n\n            | empty empty\n    \n    condicion1 : IF cond1Aux1 ENDIF PUNTOCOMA\n    \n    cond1Aux1 : cond1Aux2 IFELSE LLAVE_IZQ expresion LLAVE_DER\n            | empty empty empty empty empty\n    \n    cond1Aux2 : WHILE ID condicion sentencia THEN LLAVE_IZQ expresion LLAVE_DER cond1Aux2\n            | empty empty empty empty empty empty empty empty empty\n    \n    condicion2 : IF ID cond2Aux1 ENDIF PUNTOCOMA\n    \n    cond2Aux1 : cond2Aux2 IFELSE LLAVE_IZQ expresion LLAVE_DER\n                | empty empty empty empty empty\n    \n        cond2Aux2 : WHILE  condicion sentencia THEN LLAVE_IZQ expresion LLAVE_DER cond2Aux2\n                | empty empty empty empty empty empty empty empty\n        \n    condicion : IGUAL\n              | MAYOR\n              | MENOR\n              | DIFERENTE\n              | MAYORIGUAL\n              | MENORIGUAL\n    \n    sentencia : ID\n               | NUMERO\n    \n     repita : REPEAT LLAVE_IZQ expresion LLAVE_DER PUNTOCOMA\n    \n    hacer : RUN LLAVE_IZQ expresion LLAVE_DER  PUNTOCOMA\n    \n    funcion : Random\n            | Mover\n            | funcionAlge\n    \n    Random : RANDOM PARENTESIS_IZQ sentencia PARENTESIS_DER PUNTOCOMA\n    \n    Mover : MOVER PARENTESIS_IZQ paramMover PARENTESIS_DER PUNTOCOMA\n    \n   paramMover : AF\n                | F\n                | DFA\n                | IFA\n                | DFB\n                | IFB\n                | A\n                | DAA\n                | IAA\n                | DAB\n                | IAB\n                | AA\n    \n    funcionAlge : INC PARENTESIS_IZQ ID COMA sentencia PARENTESIS_DER PUNTOCOMA\n             | DEC PARENTESIS_IZQ ID COMA sentencia PARENTESIS_DER PUNTOCOMA\n             | INI PARENTESIS_IZQ ID COMA sentencia PARENTESIS_DER PUNTOCOMA\n    \n        procedimiento : PROC ID PARENTESIS_IZQ parametro PARENTESIS_DER PARA DOSPUNTOS expresion FIN PUNTOCOMA procedimiento\n                     | empty empty empty empty empty empty empty empty empty empty empty\n    \n    parametro : ID COMA parametro\n              | ID empty empty\n              | NUMERO COMA parametro\n              | NUMERO empty empty\n              | empty empty empty\n\n    \n    empty :\n    '
    
_lr_action_items = {'START':([0,],[3,]),'$end':([1,2,51,84,86,110,127,141,156,167,173,181,185,188,189,192,193,],[0,-1,-63,-2,-63,-63,-63,-63,-63,-63,-63,-63,-63,-63,-63,-56,-57,]),'DOSPUNTOS':([3,163,],[4,172,]),'DEF':([4,8,9,53,111,],[16,16,16,-8,-9,]),'END':([4,5,6,7,8,9,10,11,12,13,14,15,20,21,22,29,30,31,32,33,34,35,36,37,52,53,88,111,112,119,120,121,122,147,148,149,],[-63,28,-3,-4,-63,-63,-63,-63,-63,-63,-63,-63,-36,-37,-38,-5,-6,-7,-10,-63,-11,-12,-13,-14,-15,-8,-16,-9,-21,-34,-35,-39,-40,-53,-54,-55,]),'IF':([4,8,9,11,12,13,14,15,20,21,22,44,45,53,88,99,111,112,113,119,120,121,122,144,146,147,148,149,172,],[17,17,17,17,17,17,17,17,-36,-37,-38,17,17,-8,-16,17,-9,-21,17,-34,-35,-39,-40,17,17,-53,-54,-55,17,]),'REPEAT':([4,8,9,11,12,13,14,15,20,21,22,44,45,53,88,99,111,112,113,119,120,121,122,144,146,147,148,149,172,],[18,18,18,18,18,18,18,18,-36,-37,-38,18,18,-8,-16,18,-9,-21,18,-34,-35,-39,-40,18,18,-53,-54,-55,18,]),'RUN':([4,8,9,11,12,13,14,15,20,21,22,44,45,53,88,99,111,112,113,119,120,121,122,144,146,147,148,149,172,],[19,19,19,19,19,19,19,19,-36,-37,-38,19,19,-8,-16,19,-9,-21,19,-34,-35,-39,-40,19,19,-53,-54,-55,19,]),'RANDOM':([4,8,9,11,12,13,14,15,20,21,22,44,45,53,88,99,111,112,113,119,120,121,122,144,146,147,148,149,172,],[23,23,23,23,23,23,23,23,-36,-37,-38,23,23,-8,-16,23,-9,-21,23,-34,-35,-39,-40,23,23,-53,-54,-55,23,]),'MOVER':([4,8,9,11,12,13,14,15,20,21,22,44,45,53,88,99,111,112,113,119,120,121,122,144,146,147,148,149,172,],[24,24,24,24,24,24,24,24,-36,-37,-38,24,24,-8,-16,24,-9,-21,24,-34,-35,-39,-40,24,24,-53,-54,-55,24,]),'INC':([4,8,9,11,12,13,14,15,20,21,22,44,45,53,88,99,111,112,113,119,120,121,122,144,146,147,148,149,172,],[25,25,25,25,25,25,25,25,-36,-37,-38,25,25,-8,-16,25,-9,-21,25,-34,-35,-39,-40,25,25,-53,-54,-55,25,]),'DEC':([4,8,9,11,12,13,14,15,20,21,22,44,45,53,88,99,111,112,113,119,120,121,122,144,146,147,148,149,172,],[26,26,26,26,26,26,26,26,-36,-37,-38,26,26,-8,-16,26,-9,-21,26,-34,-35,-39,-40,26,26,-53,-54,-55,26,]),'INI':([4,8,9,11,12,13,14,15,20,21,22,44,45,53,88,99,111,112,113,119,120,121,122,144,146,147,148,149,172,],[27,27,27,27,27,27,27,27,-36,-37,-38,27,27,-8,-16,27,-9,-21,27,-34,-35,-39,-40,27,27,-53,-54,-55,27,]),'LLAVE_DER':([11,12,13,14,15,20,21,22,32,33,34,35,36,37,44,45,52,63,64,88,99,112,113,116,119,120,121,122,128,144,146,147,148,149,158,160,],[-63,-63,-63,-63,-63,-36,-37,-38,-10,-63,-11,-12,-13,-14,-63,-63,-15,102,103,-16,-63,-21,-63,131,-34,-35,-39,-40,142,-63,-63,-53,-54,-55,169,171,]),'FIN':([11,12,13,14,15,20,21,22,32,33,34,35,36,37,52,88,112,119,120,121,122,147,148,149,172,180,],[-63,-63,-63,-63,-63,-36,-37,-38,-10,-63,-11,-12,-13,-14,-15,-16,-21,-34,-35,-39,-40,-53,-54,-55,-63,184,]),'ID':([16,17,43,46,48,49,50,85,92,93,94,95,96,97,98,101,106,107,108,126,150,154,],[38,40,62,66,81,82,83,109,66,-26,-27,-28,-29,-30,-31,66,66,66,66,137,137,137,]),'WHILE':([17,40,169,171,],[43,59,59,43,]),'ENDIF':([17,39,40,42,56,58,61,91,100,114,117,129,131,132,142,143,],[-63,55,-63,-63,89,-63,-63,-63,-63,-63,-63,-63,-17,-18,-22,-23,]),'IFELSE':([17,40,41,42,57,58,61,91,100,114,117,129,132,143,145,157,159,168,169,170,171,174,175,176,177,178,179,182,183,186,187,190,191,194,195,],[-63,-63,60,-63,90,-63,-63,-63,-63,-63,-63,-63,-63,-63,-63,-63,-63,-63,-63,-63,-63,-25,-24,-63,-20,-19,-63,-63,-63,-63,-63,-63,-63,-63,-63,]),'LLAVE_IZQ':([18,19,60,90,130,133,],[44,45,99,113,144,146,]),'PARENTESIS_IZQ':([23,24,25,26,27,109,],[46,47,48,49,50,126,]),'PUNTOCOMA':([28,38,55,87,89,102,103,104,105,134,135,136,184,],[51,53,88,111,112,119,120,121,122,147,148,149,188,]),'DEFAULT':([38,],[54,]),'NUMERO':([46,54,92,93,94,95,96,97,98,101,106,107,108,126,150,154,],[67,87,67,-26,-27,-28,-29,-30,-31,67,67,67,67,140,140,140,]),'AF':([47,],[69,]),'F':([47,],[70,]),'DFA':([47,],[71,]),'IFA':([47,],[72,]),'DFB':([47,],[73,]),'IFB':([47,],[74,]),'A':([47,],[75,]),'DAA':([47,],[76,]),'IAA':([47,],[77,]),'DAB':([47,],[78,]),'IAB':([47,],[79,]),'AA':([47,],[80,]),'PROC':([51,188,],[85,85,]),'IGUAL':([59,62,],[93,93,]),'MAYOR':([59,62,],[94,94,]),'MENOR':([59,62,],[95,95,]),'DIFERENTE':([59,62,],[96,96,]),'MAYORIGUAL':([59,62,],[97,97,]),'MENORIGUAL':([59,62,],[98,98,]),'PARENTESIS_DER':([65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,123,124,125,126,137,138,139,140,150,151,153,154,155,161,162,164,165,166,],[104,-32,-33,105,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,134,135,136,-63,-63,152,-63,-63,-63,-63,-63,-63,-63,-58,-59,-62,-60,-61,]),'THEN':([66,67,115,118,],[-32,-33,130,133,]),'COMA':([81,82,83,137,140,],[106,107,108,150,154,]),'PARA':([152,],[163,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Start':([0,],[1,]),'code':([0,],[2,]),'cuerpo':([4,8,9,],[5,29,30,]),'variable':([4,8,9,],[6,6,6,]),'expresion':([4,8,9,11,12,13,14,15,44,45,99,113,144,146,172,],[7,7,7,32,34,35,36,37,63,64,116,128,158,160,180,]),'variable1':([4,8,9,],[8,8,8,]),'variable2':([4,8,9,],[9,9,9,]),'empty':([4,8,9,10,11,12,13,14,15,17,33,40,42,44,45,51,58,61,86,91,99,100,110,113,114,117,126,127,129,132,137,139,140,141,143,144,145,146,150,151,153,154,155,156,157,159,167,168,169,170,171,172,173,176,179,181,182,183,185,186,187,188,189,190,191,194,195,],[10,10,10,31,33,33,33,33,33,42,52,58,61,33,33,86,91,100,110,114,33,117,127,33,129,132,139,141,143,145,151,153,155,156,157,33,159,33,139,162,164,139,166,167,168,170,173,174,176,177,179,33,181,182,183,185,186,187,189,190,191,86,193,194,195,157,145,]),'condicion1':([4,8,9,11,12,13,14,15,44,45,99,113,144,146,172,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'condicion2':([4,8,9,11,12,13,14,15,44,45,99,113,144,146,172,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'repita':([4,8,9,11,12,13,14,15,44,45,99,113,144,146,172,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'hacer':([4,8,9,11,12,13,14,15,44,45,99,113,144,146,172,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'funcion':([4,8,9,11,12,13,14,15,44,45,99,113,144,146,172,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'Random':([4,8,9,11,12,13,14,15,44,45,99,113,144,146,172,],[20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'Mover':([4,8,9,11,12,13,14,15,44,45,99,113,144,146,172,],[21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'funcionAlge':([4,8,9,11,12,13,14,15,44,45,99,113,144,146,172,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'cond1Aux1':([17,],[39,]),'cond1Aux2':([17,171,],[41,178,]),'cond2Aux1':([40,],[56,]),'cond2Aux2':([40,169,],[57,175,]),'sentencia':([46,92,101,106,107,108,],[65,115,118,123,124,125,]),'paramMover':([47,],[68,]),'procedimiento':([51,188,],[84,192,]),'condicion':([59,62,],[92,101,]),'parametro':([126,150,154,],[138,161,165,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Start","S'",1,None,None,None),
  ('Start -> code','Start',1,'p_Start','Parser.py',14),
  ('code -> START DOSPUNTOS cuerpo END PUNTOCOMA procedimiento','code',6,'p_Code','Parser.py',20),
  ('cuerpo -> variable','cuerpo',1,'p_cuerpo','Parser.py',28),
  ('cuerpo -> expresion','cuerpo',1,'p_cuerpo','Parser.py',29),
  ('variable -> variable1 cuerpo','variable',2,'p_Variable','Parser.py',36),
  ('variable -> variable2 cuerpo','variable',2,'p_Variable','Parser.py',37),
  ('variable -> empty empty','variable',2,'p_Variable','Parser.py',38),
  ('variable1 -> DEF ID PUNTOCOMA','variable1',3,'p_Variable1','Parser.py',49),
  ('variable2 -> DEF ID DEFAULT NUMERO PUNTOCOMA','variable2',5,'p_Variable2','Parser.py',56),
  ('expresion -> condicion1 expresion','expresion',2,'p_expresion','Parser.py',63),
  ('expresion -> condicion2 expresion','expresion',2,'p_expresion','Parser.py',64),
  ('expresion -> repita expresion','expresion',2,'p_expresion','Parser.py',65),
  ('expresion -> hacer expresion','expresion',2,'p_expresion','Parser.py',66),
  ('expresion -> funcion expresion','expresion',2,'p_expresion','Parser.py',67),
  ('expresion -> empty empty','expresion',2,'p_expresion','Parser.py',69),
  ('condicion1 -> IF cond1Aux1 ENDIF PUNTOCOMA','condicion1',4,'p_condicion1','Parser.py',80),
  ('cond1Aux1 -> cond1Aux2 IFELSE LLAVE_IZQ expresion LLAVE_DER','cond1Aux1',5,'p_cond1Aux1','Parser.py',87),
  ('cond1Aux1 -> empty empty empty empty empty','cond1Aux1',5,'p_cond1Aux1','Parser.py',88),
  ('cond1Aux2 -> WHILE ID condicion sentencia THEN LLAVE_IZQ expresion LLAVE_DER cond1Aux2','cond1Aux2',9,'p_cond1Aux2','Parser.py',98),
  ('cond1Aux2 -> empty empty empty empty empty empty empty empty empty','cond1Aux2',9,'p_cond1Aux2','Parser.py',99),
  ('condicion2 -> IF ID cond2Aux1 ENDIF PUNTOCOMA','condicion2',5,'p_condicion2','Parser.py',111),
  ('cond2Aux1 -> cond2Aux2 IFELSE LLAVE_IZQ expresion LLAVE_DER','cond2Aux1',5,'p_cond2Aux1','Parser.py',118),
  ('cond2Aux1 -> empty empty empty empty empty','cond2Aux1',5,'p_cond2Aux1','Parser.py',119),
  ('cond2Aux2 -> WHILE condicion sentencia THEN LLAVE_IZQ expresion LLAVE_DER cond2Aux2','cond2Aux2',8,'p_cond2Aux2','Parser.py',129),
  ('cond2Aux2 -> empty empty empty empty empty empty empty empty','cond2Aux2',8,'p_cond2Aux2','Parser.py',130),
  ('condicion -> IGUAL','condicion',1,'p_condicion','Parser.py',142),
  ('condicion -> MAYOR','condicion',1,'p_condicion','Parser.py',143),
  ('condicion -> MENOR','condicion',1,'p_condicion','Parser.py',144),
  ('condicion -> DIFERENTE','condicion',1,'p_condicion','Parser.py',145),
  ('condicion -> MAYORIGUAL','condicion',1,'p_condicion','Parser.py',146),
  ('condicion -> MENORIGUAL','condicion',1,'p_condicion','Parser.py',147),
  ('sentencia -> ID','sentencia',1,'p_sentencia','Parser.py',155),
  ('sentencia -> NUMERO','sentencia',1,'p_sentencia','Parser.py',156),
  ('repita -> REPEAT LLAVE_IZQ expresion LLAVE_DER PUNTOCOMA','repita',5,'p_repita','Parser.py',163),
  ('hacer -> RUN LLAVE_IZQ expresion LLAVE_DER PUNTOCOMA','hacer',5,'p_hacer','Parser.py',170),
  ('funcion -> Random','funcion',1,'p_funcion','Parser.py',178),
  ('funcion -> Mover','funcion',1,'p_funcion','Parser.py',179),
  ('funcion -> funcionAlge','funcion',1,'p_funcion','Parser.py',180),
  ('Random -> RANDOM PARENTESIS_IZQ sentencia PARENTESIS_DER PUNTOCOMA','Random',5,'p_random','Parser.py',187),
  ('Mover -> MOVER PARENTESIS_IZQ paramMover PARENTESIS_DER PUNTOCOMA','Mover',5,'p_mover','Parser.py',194),
  ('paramMover -> AF','paramMover',1,'p_ParamMover','Parser.py',201),
  ('paramMover -> F','paramMover',1,'p_ParamMover','Parser.py',202),
  ('paramMover -> DFA','paramMover',1,'p_ParamMover','Parser.py',203),
  ('paramMover -> IFA','paramMover',1,'p_ParamMover','Parser.py',204),
  ('paramMover -> DFB','paramMover',1,'p_ParamMover','Parser.py',205),
  ('paramMover -> IFB','paramMover',1,'p_ParamMover','Parser.py',206),
  ('paramMover -> A','paramMover',1,'p_ParamMover','Parser.py',207),
  ('paramMover -> DAA','paramMover',1,'p_ParamMover','Parser.py',208),
  ('paramMover -> IAA','paramMover',1,'p_ParamMover','Parser.py',209),
  ('paramMover -> DAB','paramMover',1,'p_ParamMover','Parser.py',210),
  ('paramMover -> IAB','paramMover',1,'p_ParamMover','Parser.py',211),
  ('paramMover -> AA','paramMover',1,'p_ParamMover','Parser.py',212),
  ('funcionAlge -> INC PARENTESIS_IZQ ID COMA sentencia PARENTESIS_DER PUNTOCOMA','funcionAlge',7,'p_funcion_Alge','Parser.py',219),
  ('funcionAlge -> DEC PARENTESIS_IZQ ID COMA sentencia PARENTESIS_DER PUNTOCOMA','funcionAlge',7,'p_funcion_Alge','Parser.py',220),
  ('funcionAlge -> INI PARENTESIS_IZQ ID COMA sentencia PARENTESIS_DER PUNTOCOMA','funcionAlge',7,'p_funcion_Alge','Parser.py',221),
  ('procedimiento -> PROC ID PARENTESIS_IZQ parametro PARENTESIS_DER PARA DOSPUNTOS expresion FIN PUNTOCOMA procedimiento','procedimiento',11,'p_procedimiento','Parser.py',229),
  ('procedimiento -> empty empty empty empty empty empty empty empty empty empty empty','procedimiento',11,'p_procedimiento','Parser.py',230),
  ('parametro -> ID COMA parametro','parametro',3,'p_parametro','Parser.py',242),
  ('parametro -> ID empty empty','parametro',3,'p_parametro','Parser.py',243),
  ('parametro -> NUMERO COMA parametro','parametro',3,'p_parametro','Parser.py',244),
  ('parametro -> NUMERO empty empty','parametro',3,'p_parametro','Parser.py',245),
  ('parametro -> empty empty empty','parametro',3,'p_parametro','Parser.py',246),
  ('empty -> <empty>','empty',0,'p_empty','Parser.py',264),
]