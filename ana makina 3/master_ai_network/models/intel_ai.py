class IntelAI:
    def analyze_enemy_activity(self, data):
        """
        Düşman hareketlerini analiz eder ve tehdit seviyesini tahmin eder.
        """
        # Örnek analiz
        threat_level = "Yüksek" if "enemy_movement" in data else "Düşük"
        return {"threat_level": threat_level}
