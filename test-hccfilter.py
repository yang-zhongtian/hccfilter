from flask import Flask, render_template, jsonify, request
from filter import DFAFilter
app = Flask(__name__)

app.config["SECRET_KEY"] = "secret!"  # 需要修改
gfw = DFAFilter()
gfw.parse("keywords")


@app.route("/", methods=["GET", "POST"])
def layout():
    if request.method == "GET":
        return """
            <h1>敏感词过滤测试</h1>
            <form method="POST">
                <input type="text" name="wd" placeholder="test input" style="width:400px;" autofocus="autofocus"></input>
                <input type="submit"></input>
            </form>
        """
    else:
        wd = request.form.get("wd", "")
        res = gfw.filter(wd)
        return """
            <h1>敏感词过滤测试</h1>
            <form method="POST">
                <input type="text" name="wd" placeholder="test input" style="width:400px;" autofocus="autofocus"></input>
                <input type="submit"></input>
            </form>
            <h2>过滤结果：{}</h2>
            <h2>是否检测到敏感词：{}</h2>
        """.format(res[0],res[1])


if __name__ == "__main__":
    app.run(debug=False)
