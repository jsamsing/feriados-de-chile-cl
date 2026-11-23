# Feriados de Chile — feriados-de-chile.cl

Sitio útil de SearchLab (repo público: sin datos privados ni credenciales aquí): feriados de Chile por año, ¿hoy/mañana es feriado?, próximo feriado, irrenunciables, regionales y fines de semana largos. Avisos de la casa SOLO a searchlab.cl y Bifrok (resuelvealtiro.cl cuando esté publicado); nunca Pieza al Tiro ni ELCOM.

## Stack
- `content.py` (texto y `FERIADOS` por año, verificados con la ley vigente) + `templates/` (Jinja2, CSS y JS inline) → `python3 build.py` → `dist/`. El build FALLA si title fuera de 50-60, description fuera de 100-160, JSON-LD inválido o enlace interno roto. Fines de semana largos se calculan solos.
- Publicación: la acción «Sitios útiles (publicar)» del repo privado de SearchLab revisa este repo cada 15 min, construye y sube por SSH. Sin claves aquí.
- Año nuevo: agregar `FERIADOS[año]` y `REGIONALES[año]` con la ley vigente (traslados a lunes Ley 19.668, 17 de septiembre adicional si el 18 cae sábado o martes, 31 de octubre Ley 20.299, Pueblos Indígenas = solsticio de invierno Ley 21.357) y su página `/feriados-AAAA/`; revisar con cada ley nueva y actualizar `REVISADO`.
- Keywords con volumen (Semrush 2026-11): feriados chile 2026 165k, feriados chile 60k, feriados 2026 33k, hoy/mañana es feriado 6,6k, feriados por mes (junio 2026 12k), feriado 17 de septiembre 8k. Próximas páginas: por mes, irrenunciables, «hoy es feriado».
- Red de sitios útiles (`RED`): se enlazan entre sí solo los ya publicados.
- Menú móvil: hamburguesa a la DERECHA, panel desde la derecha, enlaces de 48 px.
