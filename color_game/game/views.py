import random
from django.shortcuts import render
from django.http import JsonResponse


# 合成ロジック（フロントと同じ）
def _mix_from_percent(pr, pg, pb):
    total = pr + pg + pb
    if total == 0:
        return 0, 0, 0
    rr = (255 * pr) // total
    gg = (255 * pg) // total
    bb = (255 * pb) // total
    return rr, gg, bb


def index(request):
    # サーバ側で「蛇口の割合」をランダムに生成（0-100）
    pr = random.randint(0, 100)
    pg = random.randint(0, 100)
    pb = random.randint(0, 100)
    # 全部0にならないように保証
    if pr + pg + pb == 0:
        pb = 1

    rr, gg, bb = _mix_from_percent(pr, pg, pb)

    # テンプレートには割合と合成RGBの両方を渡す（整合性確保）
    target = {
        "p_r": pr,
        "p_g": pg,
        "p_b": pb,
        "r": rr,
        "g": gg,
        "b": bb,
    }
    return render(request, "game/index.html", {"target": target})


def judge(request):
    # クライアントから送られた割合 (pr/pg/pb) があればそれを優先してお題RGBを再現
    pr = request.GET.get("pr")
    pg = request.GET.get("pg")
    pb = request.GET.get("pb")

    try:
        if pr is not None and pg is not None and pb is not None:
            pr_i = int(pr)
            pg_i = int(pg)
            pb_i = int(pb)
            tr, tg, tb = _mix_from_percent(pr_i, pg_i, pb_i)
            target_percent = {"p_r": pr_i, "p_g": pg_i, "p_b": pb_i}
        else:
            tr = int(request.GET.get("tr", 0))
            tg = int(request.GET.get("tg", 0))
            tb = int(request.GET.get("tb", 0))
            target_percent = None
        r = int(request.GET.get("r", 0))
        g = int(request.GET.get("g", 0))
        b = int(request.GET.get("b", 0))
    except (ValueError, TypeError):
        return JsonResponse({"error": "invalid parameters"}, status=400)

    diff = abs(r - tr) + abs(g - tg) + abs(b - tb)

    if diff < 30:
        rank = "A"
    elif diff <= 60:
        rank = "B"
    else:
        rank = "C"

    clear = diff < 30

    resp = {
        "diff": diff,
        "clear": clear,
        "rank": rank,
        "target": {"r": tr, "g": tg, "b": tb},
    }
    if target_percent is not None:
        resp["target_percent"] = target_percent

    return JsonResponse(resp)
