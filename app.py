def _run_scan(watchlist, cfg):
    E.SWEEP_WICK_MIN = float(cfg["wick_min"])
    total, results = len(watchlist), []
    pb = st.progress(0, text="تهيئة الرادار…")

    def scan_one(pair):
        ticker, smt = pair
        try:
            res = E.run_engine(
                ticker, smt,
                cfg["htf_interval"], cfg["exec_interval"],
                cfg["entry_interval"], cfg["htf_period"],
                cfg["exec_period"]
            )
            return E.extract_row(res[0], ticker, smt)
        except Exception:
            return {
                "Ticker": ticker,
                "SMT": smt,
                "Grade": "ERR",
                "Score": "—",
                "Bias": "ERROR",
                "Entry": "—",
                "SL": "—",
                "TP1": "—",
                "TP2": "—",
                "Potential R:R": "—",
                "DOL": "—",
                "SMT Signal": "—",
                "Fractal": "—",
                "Killzone": "—",
                "PD Array": "—",
                "_score_num": -1,
                "_grade_rank": 100
            }

    done = 0
    with ThreadPoolExecutor(max_workers=4) as pool:
        futures = {pool.submit(scan_one, pair): pair for pair in watchlist}
        for fut in as_completed(futures):
            tkr, smt = futures[fut]
            try:
                row = fut.result(timeout=25)
            except TimeoutError:
                row = {
                    "Ticker": tkr,
                    "SMT": smt,
                    "Grade": "TIMEOUT",
                    "Score": "—",
                    "Bias": "—",
                    "Entry": "—",
                    "SL": "—",
                    "TP1": "—",
                    "TP2": "—",
                    "Potential R:R": "—",
                    "DOL": "—",
                    "SMT Signal": "—",
                    "Fractal": "—",
                    "Killzone": "—",
                    "PD Array": "—",
                    "_score_num": -2,
                    "_grade_rank": 101
                }

            results.append(row)
            done += 1
            pb.progress(done / total, text=f"مسح {done}/{total} · {tkr}")

    pb.empty()

    df = (
        pd.DataFrame(results)
        .sort_values(by=["_grade_rank", "_score_num"], ascending=[True, False])
        .reset_index(drop=True)
    )

    st.session_state.radar_df = df
    st.session_state.radar_ts = datetime.now(timezone.utc)

    st.success(f"تم الانتهاء من المسح: {len(df)} سهم")
