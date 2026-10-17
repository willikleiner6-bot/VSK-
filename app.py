def init_db():
conn = get_db()
with open(os.path.join(os.path.dirname(file), "schema.sql")) as f:
conn.executescript(f.read())
conn.commit()
conn.close()

@app.route("/")
def dashboard():
conn = get_db()
veranstaltungen = conn.execute("SELECT * FROM veranstaltungen ORDER BY datum ASC").fetchall()
anzahl_laufend = conn.execute(
"SELECT COUNT() FROM veranstaltungen WHERE status IN ('bestaetigt','in_vorbereitung')"
).fetchone()[0]
anzahl_offene_bewerbungen = conn.execute(
"SELECT COUNT() FROM veranstalter WHERE status = 'kontaktiert'"
).fetchone()[0]
conn.close()
return render_template(
"dashboard.html",
veranstaltungen=veranstaltungen,
anzahl_laufend=anzahl_laufend,
anzahl_offene_bewerbungen=anzahl_offene_bewerbungen,
)

@app.route("/veranstaltungen/neu", methods=["GET", "POST"])
def neue_veranstaltung():
if request.method == "POST":
conn = get_db()
conn.execute(
"INSERT INTO veranstaltungen (name, datum, ort, status, kunde, budget, notizen) VALUES (?,?,?,?,?,?,?)",
(
request.form["name"],
request.form["datum"],
request.form["ort"],
request.form["status"],
request.form["kunde"],
request.form.get("budget") or 0,
request.form.get("notizen", ""),
),
)
conn.commit()
conn.close()
return redirect(url_for("dashboard"))
return render_template("neue_veranstaltung.html")

@app.route("/bewerbungen")
def bewerbungen():
conn = get_db()
veranstalter = conn.execute("SELECT * FROM veranstalter ORDER BY letzter_kontakt DESC").fetchall()
conn.close()
return render_template("bewerbungen.html", veranstalter=veranstalter)

if name == "main":
if not os.path.exists(DB_PATH):
init_db()
app.run(debug=True)
