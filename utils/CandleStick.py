from PIL import Image
import numpy as np

# NB. price info has to be a DataFrame with the following schema
#           ┌───────────────────────────────────────────────────────────┐
#           │                           DataFrame                       │
#           ├───────────────┬──────────┬──────────┬──────────┬──────────┤
# Index     │   Open        │   High   │   Low    │  Close   │   Vol    │
# ──────────┼───────────────┼──────────┼──────────┼──────────┼──────────┤
# DateTime  │   float64     │ float64  │ float64  │ float64  │   int64  │
#           └───────────────┴──────────┴──────────┴──────────┴──────────┘

class CandleStick():
    def __init__(self, price_info):
        self.price_info = price_info

    def step1_choose_window_to_plot(self, start, end, horizon_start, horizon_end, drop_vol = True):
        self.current_window = self.price_info.loc[start:end].copy()
        self.horizon_start = self.price_info.loc[horizon_start]
        self.horizon_end = self.price_info.loc[horizon_end]
        if drop_vol:
            self.current_window.drop(["Vol"], axis = 1, inplace = True)

    def step2_scale_window(self):
        _max = max(self.current_window.max())
        _min = min(self.current_window.min())
        self.current_window_scaled = self.current_window.to_numpy()
        self.current_window_scaled = np.round(((self.current_window_scaled - _min)/(_max - _min))*100)
        self.current_window_scaled = self.current_window_scaled.astype(int)
        self.current_window_scaled = 100 - self.current_window_scaled

    def step3_create_image(self):
        width, height = len(self.current_window_scaled) * 3, 100
        self.image = Image.new("RGB", (width, height), "black")
        pixels = self.image.load()
        
        for x in range(width):
            idx = x // 3
            if idx >= len(self.current_window_scaled):
                break  # Prevent index out of range
            
            current_candle = self.current_window_scaled[idx]
            open_px = current_candle[0]
            max_px = current_candle[1]
            min_px = current_candle[2]
            close_px = current_candle[3]
    
            # Draw candle body ------------------------------------------------
            color_body = (0, 255, 0) if open_px > close_px else (255, 0, 0)
            start_body = max(0, min(open_px, close_px))  # Ensure within bounds
            end_body = min(height - 1, max(open_px, close_px))  # Ensure within bounds
            
            for y in range(start_body, end_body + 1):
                if 0 <= y < height:
                    pixels[x, y] = color_body
    
        # Draw candle wick ------------------------------------------------
        for x in range(1, width, 3):
            idx = x // 3
            if idx >= len(self.current_window_scaled):
                break  # Prevent index out of range
            
            current_candle = self.current_window_scaled[idx]
            open_px = current_candle[0]
            max_px = current_candle[1]
            min_px = current_candle[2]
            close_px = current_candle[3]
    
            color_wick = (0, 255, 0) if open_px > close_px else (255, 0, 0)
    
            # Upper wick
            upper_wick_start = max(0, min(open_px, close_px))  # Ensure within bounds
            for y in range(max_px, upper_wick_start):
                if 0 <= y < height:
                    pixels[x, y] = color_wick
    
            # Lower wick
            lower_wick_start = min(height - 1, max(open_px, close_px))  # Ensure within bounds
            for y in range(lower_wick_start, min_px):
                if 0 <= y < height:
                    pixels[x, y] = color_wick
    
    def step3_bis_annotate_image(self):
        start_price = self.horizon_start["Open"]
        end_price = self.horizon_end["Close"]
        self.label = True if end_price > start_price else False

    def step4_save_img(self, directory_not_complete):
        complete_directory = f"{directory_not_complete}_{self.label}.png"
        self.image.save(complete_directory)

    def step5_clear_window(self):
        del self.current_window_scaled
        del self.current_window

    def plot_window(self, start, end, horizon_start, horizon_end, directory_not_complete):
        self.step1_choose_window_to_plot(start, end, horizon_start, horizon_end)
        self.step2_scale_window()
        self.step3_create_image()
        self.step3_bis_annotate_image()
        self.step4_save_img(directory_not_complete)
        self.step5_clear_window()


# the end
