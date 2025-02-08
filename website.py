from flask import Flask, render_template, jsonify

import main

app = Flask(__name__)
dbt = main.DatabaseTables()


@app.route('/')
def main_page():
    return render_template("main.html")


@app.route('/test')
def test_page():
    return render_template("testfetch.html")


@app.route("/api/tiktok/top", methods=["GET"])
async def api_tiktok_top():
    return jsonify(await dbt.get_tiktok_top_liked_videos())


async def run_website():
    from hypercorn.asyncio import serve
    from hypercorn.config import Config

    config = Config()
    config.bind = [f"localhost:8080"]
    await serve(app, config)
