yearly_totals = infoDF.count().max()
holder = yearly_totals + holder
i += 1
if i == 9:
    total = holder
    if total == 0:
        i = 0
        print("need more data")
    else:
        holder = 0
        k = 0
        rate_mag5 = total / 9

        freq_section = rate_mag5 * total
        recurrance_interval = 1 / freq_section
        area = radius
        conditional_interval = (recurrance_interval * area) / area
        i = 0

        # while k <= total:
        #     val = (k - recurrance_interval)
        #     val = abs(val)
        #     val = val*val
        #     val2 =val2+val
        #     k += 1
        #
        #     std = val2/total
        #     val2 = 0
        # std = math.sqrt(std)
        time = 30  # adjust for years to predict risk
        aperiodicity = (std / rate_mag5) * 100
        probability = math.sqrt((recurrance_interval / (2 * math.pi * (aperiodicity * aperiodicity) * (time ^ 3))))

        probability = probability * math.exp(-(time - ((recurrance_interval) * math.exp(2))) / (
                    2 * ((aperiodicity) * math.exp(2)) * recurrance_interval * time))

        key_stats = pd.DataFrame([{"Total Damaging Events": total, "Rate of Damaging Events": rate_mag5,
                                   "Frequency of Section": freq_section, "Recurrence Interval": recurrance_interval,
                                   "Area of Section": area,
                                   "Probability": probability}])
        key_stats = key_stats.T

        print(name)
        key_stats.to_csv(f"data/key_stats_data/{name}")