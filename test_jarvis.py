"""
Unit Test Suite for Jarvis Core - 3D Embodied AI Productivity Assistant
Verifies File Integrity, Zero Em-Dash, DOM Elements, and API Key Pre-Fill.
"""

import os
import re
import unittest

BASE_DIR = "/opt/data/jarvis-core"


class TestJarvisCoreFiles(unittest.TestCase):
    def test_required_files_exist(self):
        """Pastikan seluruh berkas utama proyek ada."""
        required = ["RANCANGAN_PROYEK.md", "README.md", "index.html"]
        for fname in required:
            fpath = os.path.join(BASE_DIR, fname)
            self.assertTrue(os.path.exists(fpath), f"File {fname} harus ada di {BASE_DIR}")
            self.assertGreater(os.path.getsize(fpath), 100, f"File {fname} tidak boleh kosong")

    def test_zero_em_dash_compliance(self):
        """Memastikan tidak ada karakter em dash (\u2014) maupun en dash (\u2013)."""
        target_files = ["RANCANGAN_PROYEK.md", "README.md", "index.html"]
        for fname in target_files:
            fpath = os.path.join(BASE_DIR, fname)
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()
            em_count = content.count("\u2014")
            en_count = content.count("\u2013")
            self.assertEqual(em_count, 0, f"Ditemukan {em_count} em-dash di {fname}")
            self.assertEqual(en_count, 0, f"Ditemukan {en_count} en-dash di {fname}")


class TestJarvisHtmlStructure(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        html_path = os.path.join(BASE_DIR, "index.html")
        with open(html_path, "r", encoding="utf-8") as f:
            cls.html_content = f.read()

    def test_threejs_and_tailwind_cdn(self):
        """Memastikan Three.js dan Tailwind CSS dimuat via CDN."""
        self.assertIn("three.min.js", self.html_content, "Three.js CDN harus ada di index.html")
        self.assertIn("cdn.tailwindcss.com", self.html_content, "Tailwind CDN harus ada di index.html")

    def test_dom_elements_present(self):
        """Memastikan seluruh elemen DOM Center-Stage, Widgets, dan Controls ada."""
        required_ids = [
            "canvas-container",
            "ambient-glow",
            "temp-slider",
            "topp-slider",
            "btn-api-modal",
            "btn-json-drawer",
            "timer-card",
            "timer-display",
            "timer-progress",
            "btn-timer-toggle",
            "btn-timer-reset",
            "todo-card",
            "todo-list",
            "todo-form",
            "todo-input",
            "chat-history",
            "chat-input",
            "chat-form",
            "btn-send",
            "json-drawer",
            "json-preview",
            "api-modal",
            "api-key-input"
        ]
        for el_id in required_ids:
            pattern = rf'id=["\']{el_id}["\']'
            self.assertRegex(self.html_content, pattern, f"Element id='{el_id}' wajib ada di index.html")

    def test_api_key_security_and_storage(self):
        """Memastikan API key dikelola aman via localStorage dan tidak bocor sebagai plaintext mentah."""
        self.assertIn("userApiKey", self.html_content)
        self.assertIn("jarvis_gemini_api_key", self.html_content)
        self.assertNotIn("AQ.Ab8RN", self.html_content)

    def test_all_four_personas_configured(self):
        """Memastikan 4 persona (calm, friendly, strict, wild) terkonfigurasi di sistem otonom dan manual selector dihapus."""
        for p_key in ["calm", "friendly", "strict", "wild"]:
            self.assertIn(f'{p_key}: {{', self.html_content, f"Persona '{p_key}' harus ada di PERSONA_PRESETS")
        self.assertNotIn('id="persona-select"', self.html_content, "Manual persona selector harus sudah dihilangkan dari pengaturan")



    def test_loading_screen_and_onboarding(self):
        """Memastikan loading screen, onboarding modal, dan empty todos terkonfigurasi."""
        self.assertIn('id="loading-screen"', self.html_content)
        self.assertIn('id="onboarding-modal"', self.html_content)
        self.assertIn('id="btn-start-explore"', self.html_content)
        self.assertIn('todos: []', self.html_content)

    def test_timer_action_in_schema(self):
        """Memastikan timerAction ada di skema response Gemini."""
        self.assertIn('timerAction', self.html_content)


    def test_security_headers_and_sanitization(self):
        """Memastikan proteksi CSP, X-Content-Type-Options, dan sanitasi XSS aktif."""
        self.assertIn('Content-Security-Policy', self.html_content)
        self.assertIn('X-Content-Type-Options', self.html_content)
        self.assertIn('X-Frame-Options', self.html_content)
        self.assertIn('safeColor', self.html_content)
        self.assertIn('safeMood', self.html_content)


    def test_timer_sound_and_chime(self):
        """Memastikan synthesizer chime Web Audio API dan voice alert selesai timer ada."""
        self.assertIn('playTimerChime', self.html_content)
        self.assertIn('playTactileClick', self.html_content)
        self.assertIn('onTimerFinished', self.html_content)

if __name__ == "__main__":
    unittest.main()
