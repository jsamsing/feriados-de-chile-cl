"""Todo el texto y los datos de feriados-de-chile.cl. Feriados según la ley vigente (Ley 2.977 y modificaciones,
Ley 19.973 irrenunciables, Ley 19.668 traslados a lunes, Ley 20.299 Iglesias Evangélicas, Ley 20.983 feriado
adicional del 17 de septiembre, Ley 21.357 Pueblos Indígenas). Revisar con cada ley nueva y actualizar REVISADO."""

DOMINIO = "https://feriados-de-chile.cl"
MARCA = "Feriados de Chile"
REVISADO = "2026-11-23"
GA4 = "G-02ZCD8D2RR"
INDEXNOW_KEY = "3e9a7d1c5b2f4e8a9c0d6b1a7f3e2d5c"

I = "irrenunciable"
# (fecha, nombre, tipo, nota)  tipo: civil | religioso; I = irrenunciable para el comercio (Ley 19.973)
FERIADOS = {
    2026: [
        ("2026-01-01", "Año Nuevo", "civil", I), ("2026-04-03", "Viernes Santo", "religioso", ""), ("2026-04-04", "Sábado Santo", "religioso", ""),
        ("2026-05-01", "Día Nacional del Trabajo", "civil", I), ("2026-05-21", "Día de las Glorias Navales", "civil", ""),
        ("2026-06-21", "Día Nacional de los Pueblos Indígenas", "civil", ""), ("2026-06-29", "San Pedro y San Pablo", "religioso", ""),
        ("2026-07-16", "Día de la Virgen del Carmen", "religioso", ""), ("2026-08-15", "Asunción de la Virgen", "religioso", ""),
        ("2026-09-18", "Independencia Nacional", "civil", I), ("2026-09-19", "Día de las Glorias del Ejército", "civil", I),
        ("2026-10-12", "Encuentro de Dos Mundos", "civil", ""), ("2026-10-31", "Día de las Iglesias Evangélicas y Protestantes", "religioso", ""),
        ("2026-11-01", "Día de Todos los Santos", "religioso", ""), ("2026-12-08", "Inmaculada Concepción", "religioso", ""),
        ("2026-12-25", "Navidad", "religioso", I),
    ],
    2027: [
        ("2027-01-01", "Año Nuevo", "civil", I), ("2027-03-26", "Viernes Santo", "religioso", ""), ("2027-03-27", "Sábado Santo", "religioso", ""),
        ("2027-05-01", "Día Nacional del Trabajo", "civil", I), ("2027-05-21", "Día de las Glorias Navales", "civil", ""),
        ("2027-06-21", "Día Nacional de los Pueblos Indígenas", "civil", ""), ("2027-06-28", "San Pedro y San Pablo", "religioso", "se traslada del martes 29 al lunes 28"),
        ("2027-07-16", "Día de la Virgen del Carmen", "religioso", ""), ("2027-08-15", "Asunción de la Virgen", "religioso", ""),
        ("2027-09-17", "Feriado adicional de Fiestas Patrias", "civil", "el 18 cae sábado"), ("2027-09-18", "Independencia Nacional", "civil", I),
        ("2027-09-19", "Día de las Glorias del Ejército", "civil", I), ("2027-10-11", "Encuentro de Dos Mundos", "civil", "se traslada del martes 12 al lunes 11"),
        ("2027-10-31", "Día de las Iglesias Evangélicas y Protestantes", "religioso", ""), ("2027-11-01", "Día de Todos los Santos", "religioso", ""),
        ("2027-12-08", "Inmaculada Concepción", "religioso", ""), ("2027-12-25", "Navidad", "religioso", I),
    ],
}
REGIONALES = {
    2027: [("2027-06-07", "Asalto y Toma del Morro de Arica", "Región de Arica y Parinacota"), ("2027-08-20", "Nacimiento del Prócer de la Independencia", "Chillán y Chillán Viejo (Ñuble)")],
}

RED = [
    {"url": "https://horadechile.cl/", "nombre": "Hora de Chile", "texto": "Hora exacta y cambio de hora", "vivo": True},
    {"url": "https://feriados-de-chile.cl/", "nombre": "Feriados de Chile", "texto": "Feriados y fines de semana largos", "vivo": True},
    {"url": "https://calculadora-chile.cl/", "nombre": "Calculadora Chile", "texto": "Sueldo líquido, IVA, UF y más", "vivo": False},
    {"url": "https://formatos-chile.cl/", "nombre": "Formatos Chile", "texto": "Cartas y documentos listos para usar", "vivo": True},
]

AVISOS = [
    {"id": "searchlab", "icono": "pin", "url": "https://www.searchlab.cl/?utm_source=feriadosdechile&utm_medium=aviso&utm_campaign=casa",
     "titulo": "¿Tu negocio aparece en Google Maps?", "texto": "Página web, ficha de Google Maps y preparación para buscadores con IA desde $9.990 al mes.", "cta": "Ver planes"},
    {"id": "bifrok", "icono": "wifi", "url": "https://bifrok.com/es-cl/?utm_source=feriadosdechile&utm_medium=aviso&utm_campaign=casa",
     "titulo": "¿Te vas el fin de semana largo?", "texto": "Si hay mala señal donde vas, compara planes de internet y Starlink por comuna.", "cta": "Comparar planes"},
]

PAGINAS = [
    {"path": "/", "tpl": "home.html", "anio": 2027,
     "title": "Feriados Chile 2026 y 2027: calendario y próximo feriado",
     "desc": "Feriados de Chile 2026 y 2027 con día de la semana, fines de semana largos, irrenunciables y cuánto falta para el próximo feriado. ¿Hoy es feriado?",
     "h1": "Feriados de Chile",
     "corta": "En 2027 Chile tiene 17 feriados nacionales, 5 de ellos irrenunciables para el comercio. El próximo feriado y si hoy o mañana es feriado aparecen aquí abajo, actualizados al día.",
     "faqs": [
         ("¿Cuántos feriados tiene Chile en 2027?", "En 2027 hay 17 feriados nacionales. Se suma el viernes 17 de septiembre, feriado adicional de Fiestas Patrias porque el 18 cae sábado."),
         ("¿Cuáles son los feriados irrenunciables?", "El 1 de enero, el 1 de mayo, el 18 y 19 de septiembre y el 25 de diciembre: ese día los trabajadores del comercio no pueden ser obligados a trabajar (Ley 19.973), salvo excepciones legales."),
         ("¿Qué feriados quedan en 2026?", "Quedan dos: martes 8 de diciembre (Inmaculada Concepción) y viernes 25 de diciembre (Navidad), que forma fin de semana largo."),
         ("¿Cómo sé si hoy es feriado?", "El recuadro de esta página revisa la fecha de hoy y de mañana con la hora de Chile y te dice si es feriado y cuál."),
     ]},
    {"path": "/feriados-2027/", "tpl": "anio.html", "anio": 2027,
     "title": "Feriados 2027 Chile: 17 feriados y fines de semana largos",
     "desc": "Lista completa de feriados de Chile 2027 con día de la semana, irrenunciables, feriados regionales y los 9 fines de semana largos del año.",
     "h1": "Feriados 2027 en Chile",
     "corta": "Chile tiene 17 feriados nacionales en 2027: parte con Año Nuevo el viernes 1 de enero y termina con Navidad el sábado 25 de diciembre. Fiestas Patrias suma el viernes 17 de septiembre y queda de viernes a domingo.",
     "faqs": [
         ("¿Cuándo es Semana Santa en 2027?", "Viernes Santo es el 26 de marzo y Sábado Santo el 27 de marzo de 2027: un fin de semana largo de tres días."),
         ("¿Hay feriado el 17 de septiembre de 2027?", "Sí. Como el 18 de septiembre cae sábado, el viernes 17 es feriado adicional por ley, y Fiestas Patrias queda de viernes a domingo."),
         ("¿Qué feriados caen en fin de semana en 2027?", "El 1 de mayo y el 25 de diciembre caen sábado; el 15 de agosto y el 31 de octubre caen domingo; el 27 de marzo y el 18 y 19 de septiembre también caen sábado o domingo."),
     ]},
    {"path": "/feriados-2026/", "tpl": "anio.html", "anio": 2026,
     "title": "Feriados 2026 Chile: calendario completo y los que quedan",
     "desc": "Feriados de Chile 2026 con día de la semana e irrenunciables. Quedan el 8 de diciembre (Inmaculada Concepción) y el 25 de diciembre (Navidad).",
     "h1": "Feriados 2026 en Chile",
     "corta": "En 2026 Chile tuvo 16 feriados nacionales. Los que quedan son el martes 8 de diciembre (Inmaculada Concepción) y el viernes 25 de diciembre (Navidad), irrenunciable y con fin de semana largo.",
     "faqs": [
         ("¿El 8 de diciembre de 2026 es feriado?", "Sí, el martes 8 de diciembre de 2026 es feriado nacional por la Inmaculada Concepción. No es irrenunciable."),
         ("¿Navidad 2026 es fin de semana largo?", "Sí: el 25 de diciembre cae viernes, así que se descansa de viernes a domingo. Es feriado irrenunciable para el comercio."),
     ]},
    {"path": "/privacidad/", "tpl": "legal.html", "noindex": True,
     "title": "Privacidad y datos personales de Feriados de Chile",
     "desc": "Cómo trata Feriados de Chile tus datos según la Ley 21.719: sin registro, medición de visitas solo con tu consentimiento y cómo ejercer tus derechos.",
     "h1": "Privacidad y datos personales"},
]


# 404 amigable (Johans 2026-11-26): layout completo, buscador, enlaces más usados, noindex; build.py lo deja en /404.html (ErrorDocument)
PAGINAS.append({"path": "/404/", "tpl": "404.html", "noindex": True, "title": "Página no encontrada | " + MARCA,
    "desc": "La página que buscas no existe o cambió de dirección. Revisa los feriados de Chile, el próximo feriado y los fines de semana largos.",
    "h1": "Este día no está en el calendario", "buscar": [[x["h1"], x["path"]] for x in PAGINAS if not x.get("noindex")]})
