import pandas as pd

# -----------------------------------------------------------------------------
# 1) BASE DE HECHOS: la tabla de vehículos, embebida directamente en el código
#    (antes vivía en vehiculos.csv; la pasamos a una lista de diccionarios
#    para que el script no dependa de ningún archivo externo).
# -----------------------------------------------------------------------------
VEHICULOS = [
    {"id": 1, "marca": 'Renault', "modelo": 'Kwid', "precio": 54.9, "rango_presupuesto": '50M-60M', "proposito_principal": 'Urbano', "proposito_secundario": 'Trabajo', "tecnologia": 'Combustión', "terreno": 'Pavimento', "pasajeros": 5, "tipo_vehiculo": 'Hatchback', "transmision": 'Mecánica', "consumo": 'Bajo'},
    {"id": 2, "marca": 'Kia', "modelo": 'Picanto', "precio": 56.99, "rango_presupuesto": '50M-60M', "proposito_principal": 'Urbano', "proposito_secundario": 'Trabajo', "tecnologia": 'Combustión', "terreno": 'Pavimento', "pasajeros": 5, "tipo_vehiculo": 'Hatchback', "transmision": 'Mecánica', "consumo": 'Bajo'},
    {"id": 3, "marca": 'Hyundai', "modelo": 'Grand i10', "precio": 67.99, "rango_presupuesto": '60M-70M', "proposito_principal": 'Urbano', "proposito_secundario": 'Trabajo', "tecnologia": 'Combustión', "terreno": 'Pavimento', "pasajeros": 5, "tipo_vehiculo": 'Hatchback', "transmision": 'Mecánica', "consumo": 'Bajo'},
    {"id": 4, "marca": 'Renault', "modelo": 'Stepway', "precio": 68.9, "rango_presupuesto": '60M-70M', "proposito_principal": 'Urbano', "proposito_secundario": 'Ninguno', "tecnologia": 'Combustión', "terreno": 'Mixto', "pasajeros": 5, "tipo_vehiculo": 'Hatchback', "transmision": 'Mecánica', "consumo": 'Medio'},
    {"id": 5, "marca": 'Volkswagen', "modelo": 'Polo Track', "precio": 79.9, "rango_presupuesto": '70M-80M', "proposito_principal": 'Urbano', "proposito_secundario": 'Ninguno', "tecnologia": 'Combustión', "terreno": 'Pavimento', "pasajeros": 5, "tipo_vehiculo": 'Hatchback', "transmision": 'Mecánica', "consumo": 'Bajo'},
    {"id": 6, "marca": 'Hyundai', "modelo": 'HB20', "precio": 79.99, "rango_presupuesto": '70M-80M', "proposito_principal": 'Urbano', "proposito_secundario": 'Ninguno', "tecnologia": 'Combustión', "terreno": 'Pavimento', "pasajeros": 5, "tipo_vehiculo": 'Hatchback', "transmision": 'Mecánica', "consumo": 'Bajo'},
    {"id": 7, "marca": 'Renault', "modelo": 'Kardian', "precio": 79.9, "rango_presupuesto": '70M-80M', "proposito_principal": 'Urbano', "proposito_secundario": 'Familiar', "tecnologia": 'Combustión', "terreno": 'Mixto', "pasajeros": 5, "tipo_vehiculo": 'SUV', "transmision": 'Automática', "consumo": 'Bajo'},
    {"id": 8, "marca": 'Kia', "modelo": 'K3 Sedán', "precio": 79.99, "rango_presupuesto": '70M-80M', "proposito_principal": 'Urbano', "proposito_secundario": 'Ninguno', "tecnologia": 'Combustión', "terreno": 'Pavimento', "pasajeros": 5, "tipo_vehiculo": 'Sedán', "transmision": 'Automática', "consumo": 'Bajo'},
    {"id": 9, "marca": 'Kia', "modelo": 'K3 Cross', "precio": 86.99, "rango_presupuesto": '80M-90M', "proposito_principal": 'Urbano', "proposito_secundario": 'Familiar', "tecnologia": 'Combustión', "terreno": 'Mixto', "pasajeros": 5, "tipo_vehiculo": 'SUV', "transmision": 'Automática', "consumo": 'Bajo'},
    {"id": 10, "marca": 'BYD', "modelo": 'Seagull', "precio": 84.99, "rango_presupuesto": '80M-90M', "proposito_principal": 'Urbano', "proposito_secundario": 'Trabajo', "tecnologia": 'Eléctrico', "terreno": 'Pavimento', "pasajeros": 5, "tipo_vehiculo": 'Hatchback', "transmision": 'Automática', "consumo": 'Muy bajo'},
    {"id": 11, "marca": 'Suzuki', "modelo": 'Swift Hybrid', "precio": 89.99, "rango_presupuesto": '80M-90M', "proposito_principal": 'Urbano', "proposito_secundario": 'Ninguno', "tecnologia": 'Híbrido', "terreno": 'Pavimento', "pasajeros": 5, "tipo_vehiculo": 'Hatchback', "transmision": 'Automática', "consumo": 'Muy bajo'},
    {"id": 12, "marca": 'Chery', "modelo": 'Tiggo 2 Pro', "precio": 89.9, "rango_presupuesto": '80M-90M', "proposito_principal": 'Urbano', "proposito_secundario": 'Familiar', "tecnologia": 'Combustión', "terreno": 'Mixto', "pasajeros": 5, "tipo_vehiculo": 'SUV', "transmision": 'Automática', "consumo": 'Medio'},
    {"id": 13, "marca": 'Toyota', "modelo": 'Yaris Sedán', "precio": 88.5, "rango_presupuesto": '80M-90M', "proposito_principal": 'Urbano', "proposito_secundario": 'Ninguno', "tecnologia": 'Combustión', "terreno": 'Pavimento', "pasajeros": 5, "tipo_vehiculo": 'Sedán', "transmision": 'Automática', "consumo": 'Bajo'},
    {"id": 14, "marca": 'Kia', "modelo": 'Sonet', "precio": 97.99, "rango_presupuesto": '90M-100M', "proposito_principal": 'Urbano', "proposito_secundario": 'Familiar', "tecnologia": 'Combustión', "terreno": 'Mixto', "pasajeros": 5, "tipo_vehiculo": 'SUV', "transmision": 'Automática', "consumo": 'Bajo'},
    {"id": 15, "marca": 'Hyundai', "modelo": 'Venue', "precio": 98.99, "rango_presupuesto": '90M-100M', "proposito_principal": 'Urbano', "proposito_secundario": 'Familiar', "tecnologia": 'Combustión', "terreno": 'Mixto', "pasajeros": 5, "tipo_vehiculo": 'SUV', "transmision": 'Automática', "consumo": 'Bajo'},
    {"id": 16, "marca": 'Suzuki', "modelo": 'Baleno Hybrid', "precio": 95.99, "rango_presupuesto": '90M-100M', "proposito_principal": 'Urbano', "proposito_secundario": 'Ninguno', "tecnologia": 'Híbrido', "terreno": 'Pavimento', "pasajeros": 5, "tipo_vehiculo": 'Hatchback', "transmision": 'Automática', "consumo": 'Muy bajo'},
    {"id": 17, "marca": 'BYD', "modelo": 'Dolphin Mini', "precio": 96.9, "rango_presupuesto": '90M-100M', "proposito_principal": 'Urbano', "proposito_secundario": 'Ninguno', "tecnologia": 'Eléctrico', "terreno": 'Pavimento', "pasajeros": 5, "tipo_vehiculo": 'Hatchback', "transmision": 'Automática', "consumo": 'Muy bajo'},
    {"id": 18, "marca": 'BYD', "modelo": 'Yuan Up', "precio": 98.9, "rango_presupuesto": '90M-100M', "proposito_principal": 'Urbano', "proposito_secundario": 'Familiar', "tecnologia": 'Eléctrico', "terreno": 'Mixto', "pasajeros": 5, "tipo_vehiculo": 'SUV', "transmision": 'Automática', "consumo": 'Muy bajo'},
    {"id": 19, "marca": 'Mazda', "modelo": 'Mazda 2', "precio": 99.9, "rango_presupuesto": '90M-100M', "proposito_principal": 'Urbano', "proposito_secundario": 'Ninguno', "tecnologia": 'Combustión', "terreno": 'Pavimento', "pasajeros": 5, "tipo_vehiculo": 'Sedán', "transmision": 'Automática', "consumo": 'Bajo'},
    {"id": 20, "marca": 'Toyota', "modelo": 'Corolla Sedán HEV', "precio": 109.9, "rango_presupuesto": '100M-120M', "proposito_principal": 'Urbano', "proposito_secundario": 'Familiar', "tecnologia": 'Híbrido', "terreno": 'Pavimento', "pasajeros": 5, "tipo_vehiculo": 'Sedán', "transmision": 'Automática', "consumo": 'Muy bajo'},
    {"id": 21, "marca": 'Mazda', "modelo": 'Mazda 3', "precio": 116.9, "rango_presupuesto": '100M-120M', "proposito_principal": 'Urbano', "proposito_secundario": 'Ninguno', "tecnologia": 'Combustión', "terreno": 'Pavimento', "pasajeros": 5, "tipo_vehiculo": 'Sedán', "transmision": 'Automática', "consumo": 'Bajo'},
    {"id": 22, "marca": 'Mazda', "modelo": 'CX-30 MHEV', "precio": 108.9, "rango_presupuesto": '100M-120M', "proposito_principal": 'Familiar', "proposito_secundario": 'Urbano', "tecnologia": 'Mild Hybrid', "terreno": 'Mixto', "pasajeros": 5, "tipo_vehiculo": 'SUV', "transmision": 'Automática', "consumo": 'Bajo'},
    {"id": 23, "marca": 'Renault', "modelo": 'Duster', "precio": 112.9, "rango_presupuesto": '100M-120M', "proposito_principal": 'Familiar', "proposito_secundario": 'Aventura', "tecnologia": 'Combustión', "terreno": 'Mixto', "pasajeros": 5, "tipo_vehiculo": 'SUV', "transmision": 'Mecánica', "consumo": 'Medio'},
    {"id": 24, "marca": 'Volkswagen', "modelo": 'Nivus', "precio": 118.9, "rango_presupuesto": '100M-120M', "proposito_principal": 'Urbano', "proposito_secundario": 'Ninguno', "tecnologia": 'Combustión', "terreno": 'Pavimento', "pasajeros": 5, "tipo_vehiculo": 'SUV', "transmision": 'Automática', "consumo": 'Bajo'},
    {"id": 25, "marca": 'Suzuki', "modelo": 'Fronx Hybrid', "precio": 114.99, "rango_presupuesto": '100M-120M', "proposito_principal": 'Urbano', "proposito_secundario": 'Ninguno', "tecnologia": 'Híbrido', "terreno": 'Mixto', "pasajeros": 5, "tipo_vehiculo": 'SUV', "transmision": 'Automática', "consumo": 'Muy bajo'},
    {"id": 26, "marca": 'Tesla', "modelo": 'Model 3', "precio": 114.99, "rango_presupuesto": '100M-120M', "proposito_principal": 'Urbano', "proposito_secundario": 'Ninguno', "tecnologia": 'Eléctrico', "terreno": 'Pavimento', "pasajeros": 5, "tipo_vehiculo": 'Sedán', "transmision": 'Automática', "consumo": 'Muy bajo'},
    {"id": 27, "marca": 'BYD', "modelo": 'Dolphin', "precio": 109.9, "rango_presupuesto": '100M-120M', "proposito_principal": 'Urbano', "proposito_secundario": 'Ninguno', "tecnologia": 'Eléctrico', "terreno": 'Pavimento', "pasajeros": 5, "tipo_vehiculo": 'Hatchback', "transmision": 'Automática', "consumo": 'Muy bajo'},
    {"id": 28, "marca": 'Chery', "modelo": 'Tiggo 4 Pro', "precio": 109.9, "rango_presupuesto": '100M-120M', "proposito_principal": 'Familiar', "proposito_secundario": 'Ninguno', "tecnologia": 'Combustión', "terreno": 'Mixto', "pasajeros": 5, "tipo_vehiculo": 'SUV', "transmision": 'Automática', "consumo": 'Medio'},
    {"id": 29, "marca": 'Kia', "modelo": 'Seltos', "precio": 129.99, "rango_presupuesto": '120M-140M', "proposito_principal": 'Familiar', "proposito_secundario": 'Ninguno', "tecnologia": 'Combustión', "terreno": 'Mixto', "pasajeros": 5, "tipo_vehiculo": 'SUV', "transmision": 'Automática', "consumo": 'Medio'},
    {"id": 30, "marca": 'Hyundai', "modelo": 'Creta', "precio": 129.99, "rango_presupuesto": '120M-140M', "proposito_principal": 'Familiar', "proposito_secundario": 'Ninguno', "tecnologia": 'Combustión', "terreno": 'Mixto', "pasajeros": 5, "tipo_vehiculo": 'SUV', "transmision": 'Automática', "consumo": 'Medio'},
    {"id": 31, "marca": 'Suzuki', "modelo": 'Vitara Hybrid', "precio": 132.99, "rango_presupuesto": '120M-140M', "proposito_principal": 'Familiar', "proposito_secundario": 'Ninguno', "tecnologia": 'Híbrido', "terreno": 'Mixto', "pasajeros": 5, "tipo_vehiculo": 'SUV', "transmision": 'Automática', "consumo": 'Muy bajo'},
    {"id": 32, "marca": 'Volkswagen', "modelo": 'T-Cross', "precio": 135.9, "rango_presupuesto": '120M-140M', "proposito_principal": 'Familiar', "proposito_secundario": 'Ninguno', "tecnologia": 'Combustión', "terreno": 'Mixto', "pasajeros": 5, "tipo_vehiculo": 'SUV', "transmision": 'Automática', "consumo": 'Medio'},
    {"id": 33, "marca": 'Chery', "modelo": 'Tiggo 7 Pro', "precio": 139.9, "rango_presupuesto": '120M-140M', "proposito_principal": 'Familiar', "proposito_secundario": 'Ninguno', "tecnologia": 'Combustión', "terreno": 'Mixto', "pasajeros": 5, "tipo_vehiculo": 'SUV', "transmision": 'Automática', "consumo": 'Medio'},
    {"id": 34, "marca": 'BYD', "modelo": 'Yuan Pro', "precio": 128.9, "rango_presupuesto": '120M-140M', "proposito_principal": 'Familiar', "proposito_secundario": 'Ninguno', "tecnologia": 'Eléctrico', "terreno": 'Mixto', "pasajeros": 5, "tipo_vehiculo": 'SUV', "transmision": 'Automática', "consumo": 'Muy bajo'},
    {"id": 35, "marca": 'Suzuki', "modelo": 'Grand Vitara Hybrid', "precio": 158.99, "rango_presupuesto": '140M-160M', "proposito_principal": 'Familiar', "proposito_secundario": 'Ninguno', "tecnologia": 'Híbrido', "terreno": 'Mixto', "pasajeros": 5, "tipo_vehiculo": 'SUV', "transmision": 'Automática', "consumo": 'Muy bajo'},
    {"id": 36, "marca": 'Mazda', "modelo": 'CX-5', "precio": 145.0, "rango_presupuesto": '140M-160M', "proposito_principal": 'Familiar', "proposito_secundario": 'Ninguno', "tecnologia": 'Combustión', "terreno": 'Mixto', "pasajeros": 5, "tipo_vehiculo": 'SUV', "transmision": 'Automática', "consumo": 'Medio'},
    {"id": 37, "marca": 'Toyota', "modelo": 'Corolla Cross HEV', "precio": 165.0, "rango_presupuesto": '160+', "proposito_principal": 'Familiar', "proposito_secundario": 'Ninguno', "tecnologia": 'Híbrido', "terreno": 'Mixto', "pasajeros": 5, "tipo_vehiculo": 'SUV', "transmision": 'Automática', "consumo": 'Muy bajo'},
    {"id": 38, "marca": 'Kia', "modelo": 'Sportage Hybrid', "precio": 179.99, "rango_presupuesto": '160+', "proposito_principal": 'Familiar', "proposito_secundario": 'Ninguno', "tecnologia": 'Híbrido', "terreno": 'Mixto', "pasajeros": 5, "tipo_vehiculo": 'SUV', "transmision": 'Automática', "consumo": 'Muy bajo'},
    {"id": 39, "marca": 'Renault', "modelo": 'Arkana E-Tech', "precio": 170.0, "rango_presupuesto": '160+', "proposito_principal": 'Familiar', "proposito_secundario": 'Ninguno', "tecnologia": 'Híbrido', "terreno": 'Mixto', "pasajeros": 5, "tipo_vehiculo": 'SUV', "transmision": 'Automática', "consumo": 'Muy bajo'},
    {"id": 40, "marca": 'Renault', "modelo": 'Koleos', "precio": 189.9, "rango_presupuesto": '160+', "proposito_principal": 'Familiar', "proposito_secundario": 'Ninguno', "tecnologia": 'Combustión', "terreno": 'Mixto', "pasajeros": 5, "tipo_vehiculo": 'SUV', "transmision": 'Automática', "consumo": 'Medio'},
    {"id": 41, "marca": 'Volkswagen', "modelo": 'Taos', "precio": 182.9, "rango_presupuesto": '160+', "proposito_principal": 'Familiar', "proposito_secundario": 'Ninguno', "tecnologia": 'Combustión', "terreno": 'Mixto', "pasajeros": 5, "tipo_vehiculo": 'SUV', "transmision": 'Automática', "consumo": 'Medio'},
    {"id": 42, "marca": 'Volkswagen', "modelo": 'Amarok', "precio": 235.0, "rango_presupuesto": '160+', "proposito_principal": 'Trabajo', "proposito_secundario": 'Aventura', "tecnologia": 'Combustión', "terreno": 'Destapado', "pasajeros": 5, "tipo_vehiculo": 'Pickup', "transmision": 'Automática', "consumo": 'Alto'},
    {"id": 43, "marca": 'Toyota', "modelo": 'Hilux 4x2', "precio": 170.0, "rango_presupuesto": '160+', "proposito_principal": 'Trabajo', "proposito_secundario": 'Ninguno', "tecnologia": 'Combustión', "terreno": 'Mixto', "pasajeros": 5, "tipo_vehiculo": 'Pickup', "transmision": 'Mecánica', "consumo": 'Alto'},
    {"id": 44, "marca": 'Toyota', "modelo": 'Hilux 4x4', "precio": 190.0, "rango_presupuesto": '160+', "proposito_principal": 'Trabajo', "proposito_secundario": 'Aventura', "tecnologia": 'Combustión', "terreno": 'Destapado', "pasajeros": 5, "tipo_vehiculo": 'Pickup', "transmision": 'Automática', "consumo": 'Alto'},
    {"id": 45, "marca": 'Toyota', "modelo": 'Prado', "precio": 290.0, "rango_presupuesto": '160+', "proposito_principal": 'Aventura', "proposito_secundario": 'Familiar', "tecnologia": 'Combustión', "terreno": 'Destapado', "pasajeros": 7, "tipo_vehiculo": 'SUV', "transmision": 'Automática', "consumo": 'Alto'},
    {"id": 46, "marca": 'Toyota', "modelo": 'Land Cruiser 300', "precio": 430.0, "rango_presupuesto": '160+', "proposito_principal": 'Aventura', "proposito_secundario": 'Ninguno', "tecnologia": 'Combustión', "terreno": 'Destapado', "pasajeros": 7, "tipo_vehiculo": 'SUV', "transmision": 'Automática', "consumo": 'Alto'},
    {"id": 47, "marca": 'Ford', "modelo": 'Ranger XLS', "precio": 195.0, "rango_presupuesto": '160+', "proposito_principal": 'Trabajo', "proposito_secundario": 'Ninguno', "tecnologia": 'Combustión', "terreno": 'Destapado', "pasajeros": 5, "tipo_vehiculo": 'Pickup', "transmision": 'Mecánica', "consumo": 'Alto'},
    {"id": 48, "marca": 'Ford', "modelo": 'Ranger XLT', "precio": 225.0, "rango_presupuesto": '160+', "proposito_principal": 'Trabajo', "proposito_secundario": 'Aventura', "tecnologia": 'Combustión', "terreno": 'Destapado', "pasajeros": 5, "tipo_vehiculo": 'Pickup', "transmision": 'Automática', "consumo": 'Alto'},
    {"id": 49, "marca": 'Ford', "modelo": 'Ranger Limited', "precio": 260.0, "rango_presupuesto": '160+', "proposito_principal": 'Trabajo', "proposito_secundario": 'Aventura', "tecnologia": 'Combustión', "terreno": 'Destapado', "pasajeros": 5, "tipo_vehiculo": 'Pickup', "transmision": 'Automática', "consumo": 'Alto'},
    {"id": 50, "marca": 'Ford', "modelo": 'Escape Hybrid', "precio": 210.0, "rango_presupuesto": '160+', "proposito_principal": 'Familiar', "proposito_secundario": 'Ninguno', "tecnologia": 'Híbrido', "terreno": 'Mixto', "pasajeros": 5, "tipo_vehiculo": 'SUV', "transmision": 'Automática', "consumo": 'Muy bajo'},
    {"id": 51, "marca": 'Ford', "modelo": 'Explorer', "precio": 295.0, "rango_presupuesto": '160+', "proposito_principal": 'Familiar', "proposito_secundario": 'Ninguno', "tecnologia": 'Combustión', "terreno": 'Mixto', "pasajeros": 7, "tipo_vehiculo": 'SUV', "transmision": 'Automática', "consumo": 'Alto'},
    {"id": 52, "marca": 'Hyundai', "modelo": 'Tucson Hybrid', "precio": 189.9, "rango_presupuesto": '160+', "proposito_principal": 'Familiar', "proposito_secundario": 'Ninguno', "tecnologia": 'Híbrido', "terreno": 'Mixto', "pasajeros": 5, "tipo_vehiculo": 'SUV', "transmision": 'Automática', "consumo": 'Muy bajo'},
    {"id": 53, "marca": 'Hyundai', "modelo": 'Santa Fe Hybrid', "precio": 255.0, "rango_presupuesto": '160+', "proposito_principal": 'Familiar', "proposito_secundario": 'Ninguno', "tecnologia": 'Híbrido', "terreno": 'Mixto', "pasajeros": 7, "tipo_vehiculo": 'SUV', "transmision": 'Automática', "consumo": 'Muy bajo'},
    {"id": 54, "marca": 'Hyundai', "modelo": 'Kona Electric', "precio": 199.9, "rango_presupuesto": '160+', "proposito_principal": 'Urbano', "proposito_secundario": 'Ninguno', "tecnologia": 'Eléctrico', "terreno": 'Pavimento', "pasajeros": 5, "tipo_vehiculo": 'SUV', "transmision": 'Automática', "consumo": 'Muy bajo'},
    {"id": 55, "marca": 'BYD', "modelo": 'Song Pro DM-i', "precio": 169.9, "rango_presupuesto": '160+', "proposito_principal": 'Familiar', "proposito_secundario": 'Ninguno', "tecnologia": 'Híbrido Enchufable', "terreno": 'Mixto', "pasajeros": 5, "tipo_vehiculo": 'SUV', "transmision": 'Automática', "consumo": 'Muy bajo'},
    {"id": 56, "marca": 'BYD', "modelo": 'Song Plus DM-i', "precio": 189.9, "rango_presupuesto": '160+', "proposito_principal": 'Familiar', "proposito_secundario": 'Ninguno', "tecnologia": 'Híbrido Enchufable', "terreno": 'Mixto', "pasajeros": 5, "tipo_vehiculo": 'SUV', "transmision": 'Automática', "consumo": 'Muy bajo'},
    {"id": 57, "marca": 'BYD', "modelo": 'Seal', "precio": 219.9, "rango_presupuesto": '160+', "proposito_principal": 'Urbano', "proposito_secundario": 'Ninguno', "tecnologia": 'Eléctrico', "terreno": 'Pavimento', "pasajeros": 5, "tipo_vehiculo": 'Sedán', "transmision": 'Automática', "consumo": 'Muy bajo'},
    {"id": 58, "marca": 'BYD', "modelo": 'Han EV', "precio": 299.9, "rango_presupuesto": '160+', "proposito_principal": 'Familiar', "proposito_secundario": 'Ninguno', "tecnologia": 'Eléctrico', "terreno": 'Pavimento', "pasajeros": 5, "tipo_vehiculo": 'Sedán', "transmision": 'Automática', "consumo": 'Muy bajo'},
    {"id": 59, "marca": 'BYD', "modelo": 'Tang EV', "precio": 339.9, "rango_presupuesto": '160+', "proposito_principal": 'Familiar', "proposito_secundario": 'Aventura', "tecnologia": 'Eléctrico', "terreno": 'Mixto', "pasajeros": 7, "tipo_vehiculo": 'SUV', "transmision": 'Automática', "consumo": 'Muy bajo'},
    {"id": 60, "marca": 'Tesla', "modelo": 'Model Y', "precio": 199.9, "rango_presupuesto": '160+', "proposito_principal": 'Familiar', "proposito_secundario": 'Ninguno', "tecnologia": 'Eléctrico', "terreno": 'Mixto', "pasajeros": 5, "tipo_vehiculo": 'SUV', "transmision": 'Automática', "consumo": 'Muy bajo'},
    {"id": 61, "marca": 'BMW', "modelo": 'Serie 1', "precio": 189.0, "rango_presupuesto": '160+', "proposito_principal": 'Urbano', "proposito_secundario": 'Ninguno', "tecnologia": 'Combustión', "terreno": 'Pavimento', "pasajeros": 5, "tipo_vehiculo": 'Hatchback', "transmision": 'Automática', "consumo": 'Medio'},
    {"id": 62, "marca": 'BMW', "modelo": 'Serie 2 Gran Coupé', "precio": 205.0, "rango_presupuesto": '160+', "proposito_principal": 'Urbano', "proposito_secundario": 'Ninguno', "tecnologia": 'Combustión', "terreno": 'Pavimento', "pasajeros": 5, "tipo_vehiculo": 'Sedán', "transmision": 'Automática', "consumo": 'Medio'},
    {"id": 63, "marca": 'BMW', "modelo": 'X1', "precio": 239.0, "rango_presupuesto": '160+', "proposito_principal": 'Familiar', "proposito_secundario": 'Ninguno', "tecnologia": 'Combustión', "terreno": 'Mixto', "pasajeros": 5, "tipo_vehiculo": 'SUV', "transmision": 'Automática', "consumo": 'Medio'},
    {"id": 64, "marca": 'BMW', "modelo": 'iX1', "precio": 269.0, "rango_presupuesto": '160+', "proposito_principal": 'Familiar', "proposito_secundario": 'Ninguno', "tecnologia": 'Eléctrico', "terreno": 'Mixto', "pasajeros": 5, "tipo_vehiculo": 'SUV', "transmision": 'Automática', "consumo": 'Muy bajo'},
    {"id": 65, "marca": 'BMW', "modelo": 'X3', "precio": 339.0, "rango_presupuesto": '160+', "proposito_principal": 'Familiar', "proposito_secundario": 'Ninguno', "tecnologia": 'Híbrido', "terreno": 'Mixto', "pasajeros": 5, "tipo_vehiculo": 'SUV', "transmision": 'Automática', "consumo": 'Muy bajo'},
    {"id": 66, "marca": 'BMW', "modelo": 'i4', "precio": 349.0, "rango_presupuesto": '160+', "proposito_principal": 'Urbano', "proposito_secundario": 'Ninguno', "tecnologia": 'Eléctrico', "terreno": 'Pavimento', "pasajeros": 5, "tipo_vehiculo": 'Sedán', "transmision": 'Automática', "consumo": 'Muy bajo'},
    {"id": 67, "marca": 'BMW', "modelo": 'X5 PHEV', "precio": 499.0, "rango_presupuesto": '160+', "proposito_principal": 'Familiar', "proposito_secundario": 'Aventura', "tecnologia": 'Híbrido Enchufable', "terreno": 'Destapado', "pasajeros": 5, "tipo_vehiculo": 'SUV', "transmision": 'Automática', "consumo": 'Muy bajo'},
]


def cargar_vehiculos() -> pd.DataFrame:
    """Construye la base de conocimiento de vehículos a partir de VEHICULOS."""
    return pd.DataFrame(VEHICULOS)


# -----------------------------------------------------------------------------
# 2) BASE DE PESOS: cuánto vale cada criterio si hay coincidencia perfecta.
#    Esta MISMA tabla es la que exporto a Excel en la hoja "Pesos", para que
#    no queden números "mágicos" escondidos en el código.
#    Suman 100 puntos -> el puntaje final de cada vehículo queda en escala 0-100.
# -----------------------------------------------------------------------------
PESOS = {
    "presupuesto": 20,
    "tipo_vehiculo": 15,
    "proposito": 15,
    "tecnologia": 15,
    "terreno": 10,
    "pasajeros": 5,
    "transmision": 5,
    "consumo": 10,
    "marca": 5,
}

# Órdenes que necesitamos para medir "cercanía" entre categorías (no solo
# igual/distinto). Esto es lo que le da inteligencia al motor: un vehículo
# de rango 90M-100M no queda en cero frente a un usuario que pidió 100M-120M,
# porque están "cerca". Lo mismo con el nivel de consumo.
ORDEN_PRESUPUESTO = [
    "50M-60M", "60M-70M", "70M-80M", "80M-90M", "90M-100M",
    "100M-120M", "120M-140M", "140M-160M", "160+",
]
ORDEN_CONSUMO = ["Muy bajo", "Bajo", "Medio", "Alto"]

# Tabla de compatibilidad de tecnologías: si no hay match exacto, algunas
# tecnologías son "primas" entre sí (ambas son formas de electrificación),
# así que reciben un puntaje parcial en vez de cero.
TECNOLOGIAS_COMPATIBLES = {
    "Híbrido": {"Mild Hybrid", "Híbrido Enchufable"},
    "Mild Hybrid": {"Híbrido"},
    "Híbrido Enchufable": {"Híbrido", "Eléctrico"},
    "Eléctrico": {"Híbrido Enchufable"},
}


# =============================================================================
# 3) LAS REGLAS SI-ENTONCES
# =============================================================================
# Cada función de abajo es UNA regla del motor. Todas devuelven una tupla
# (puntos_obtenidos, explicacion_en_texto) para que el sistema pueda, al final,
# no solo dar el Top 3 sino JUSTIFICAR por qué quedó ahí (nodo 16 de tu mapa:
# "Explicación del resultado").
# =============================================================================

def regla_presupuesto(vehiculo, respuestas):
    """
    R1 - SI el rango de presupuesto del usuario == rango del vehículo
            ENTONCES sumar el peso completo.
         SI son rangos ADYACENTES (uno arriba o uno abajo en la escala)
            ENTONCES sumar la mitad del peso (el vehículo casi le alcanza,
            o se queda un poco corto: sigue siendo una opción razonable).
         SINO 0 puntos.
    """
    peso = PESOS["presupuesto"]
    rango_usuario = respuestas["presupuesto"]
    rango_vehiculo = vehiculo["rango_presupuesto"]

    if rango_usuario == rango_vehiculo:
        return peso, f"Presupuesto coincide exactamente ({rango_vehiculo})"

    try:
        idx_usuario = ORDEN_PRESUPUESTO.index(rango_usuario)
        idx_vehiculo = ORDEN_PRESUPUESTO.index(rango_vehiculo)
        if abs(idx_usuario - idx_vehiculo) == 1:
            return peso / 2, f"Presupuesto en rango cercano ({rango_vehiculo})"
    except ValueError:
        pass

    return 0, "Presupuesto fuera de rango"


def regla_tipo_vehiculo(vehiculo, respuestas):
    """R2 - SI tipo de vehículo deseado == tipo del vehículo ENTONCES peso completo, SINO 0."""
    peso = PESOS["tipo_vehiculo"]
    if respuestas["tipo_vehiculo"] == vehiculo["tipo_vehiculo"]:
        return peso, f"Tipo de vehículo coincide ({vehiculo['tipo_vehiculo']})"
    return 0, "Tipo de vehículo no coincide"


def regla_proposito(vehiculo, respuestas):
    """
    R3 - SI propósito del usuario == propósito PRINCIPAL del vehículo
            ENTONCES peso completo.
         SI propósito del usuario == propósito SECUNDARIO del vehículo
            ENTONCES la mitad del peso (le sirve, pero no es su fuerte).
         SINO 0.
    """
    peso = PESOS["proposito"]
    deseado = respuestas["proposito"]
    if deseado == vehiculo["proposito_principal"]:
        return peso, f"Propósito principal coincide ({deseado})"
    if deseado == vehiculo["proposito_secundario"]:
        return peso / 2, f"Propósito coincide como uso secundario ({deseado})"
    return 0, "Propósito no coincide"


def regla_tecnologia(vehiculo, respuestas):
    """
    R4 - SI tecnología deseada == tecnología del vehículo ENTONCES peso completo.
         SI la tecnología del vehículo está en la lista de "compatibles" con la
            deseada (ambas son electrificadas) ENTONCES la mitad del peso.
         SINO 0.
    """
    peso = PESOS["tecnologia"]
    deseada = respuestas["tecnologia"]
    real = vehiculo["tecnologia"]
    if deseada == real:
        return peso, f"Tecnología coincide ({real})"
    if real in TECNOLOGIAS_COMPATIBLES.get(deseada, set()):
        return peso / 2, f"Tecnología compatible/similar ({real})"
    return 0, "Tecnología no coincide"


def regla_terreno(vehiculo, respuestas):
    """
    R5 - SI terreno deseado == terreno del vehículo ENTONCES peso completo.
         SI el vehículo es "Mixto" y el usuario pidió Pavimento o Destapado
            ENTONCES puntaje alto (60%), porque "Mixto" SÍ cubre ambos casos.
         SI el usuario pidió "Mixto" pero el vehículo es solo Pavimento o
            solo Destapado ENTONCES puntaje bajo (40%), porque cubre apenas
            la mitad de lo que pidió.
         SINO 0.
    """
    peso = PESOS["terreno"]
    deseado = respuestas["terreno"]
    real = vehiculo["terreno"]

    if deseado == real:
        return peso, f"Terreno coincide ({real})"
    if real == "Mixto" and deseado in ("Pavimento", "Destapado"):
        return peso * 0.6, "Vehículo Mixto cubre el terreno solicitado"
    if deseado == "Mixto" and real in ("Pavimento", "Destapado"):
        return peso * 0.4, "Vehículo cubre solo parte del terreno mixto pedido"
    return 0, "Terreno no coincide"


def regla_pasajeros(vehiculo, respuestas):
    """R6 - SI capacidad del vehículo >= pasajeros requeridos ENTONCES peso completo, SINO 0."""
    peso = PESOS["pasajeros"]
    if vehiculo["pasajeros"] >= respuestas["pasajeros"]:
        return peso, f"Capacidad suficiente ({vehiculo['pasajeros']} puestos)"
    return 0, "Capacidad insuficiente"


def regla_transmision(vehiculo, respuestas):
    """R7 - SI transmisión deseada == transmisión del vehículo ENTONCES peso completo, SINO 0."""
    peso = PESOS["transmision"]
    if respuestas["transmision"] == vehiculo["transmision"]:
        return peso, f"Transmisión coincide ({vehiculo['transmision']})"
    return 0, "Transmisión no coincide"


def regla_consumo(vehiculo, respuestas):
    """
    R8 - SI nivel de consumo deseado == nivel del vehículo ENTONCES peso completo.
         SI está un nivel arriba o abajo en la escala Muy bajo/Bajo/Medio/Alto
            ENTONCES la mitad del peso.
         SINO 0.
    """
    peso = PESOS["consumo"]
    deseado = respuestas["consumo"]
    real = vehiculo["consumo"]
    if deseado == real:
        return peso, f"Consumo coincide ({real})"
    try:
        if abs(ORDEN_CONSUMO.index(deseado) - ORDEN_CONSUMO.index(real)) == 1:
            return peso / 2, f"Consumo cercano al deseado ({real})"
    except ValueError:
        pass
    return 0, "Consumo no coincide"


def regla_marca(vehiculo, respuestas):
    """
    R9 - SI el usuario NO seleccionó marca preferida ENTONCES la regla no aplica
            (se excluye del total posible, ver normalización en calcular_puntaje).
         SI seleccionó marca Y coincide ENTONCES peso completo.
         SINO 0.
    """
    peso = PESOS["marca"]
    marca_deseada = respuestas.get("marca")  # None si el usuario dijo "No" en el nodo 10
    if not marca_deseada:
        return None, "Marca no aplica (usuario no indicó preferencia)"
    if marca_deseada == vehiculo["marca"]:
        return peso, f"Marca preferida coincide ({vehiculo['marca']})"
    return 0, "Marca no coincide con la preferida"


# Lista de todas las reglas activas, emparejadas con su clave en PESOS.
# Agregar una regla nueva al motor es tan simple como escribir la función,
# poner su peso en PESOS y añadir el par (clave, función) aquí.
REGLAS = [
    ("presupuesto", regla_presupuesto),
    ("tipo_vehiculo", regla_tipo_vehiculo),
    ("proposito", regla_proposito),
    ("tecnologia", regla_tecnologia),
    ("terreno", regla_terreno),
    ("pasajeros", regla_pasajeros),
    ("transmision", regla_transmision),
    ("consumo", regla_consumo),
    ("marca", regla_marca),
]


# =============================================================================
# 4) MOTOR DE INFERENCIA: aplica TODAS las reglas a UN vehículo
# =============================================================================
def calcular_puntaje(vehiculo, respuestas):
    """
    Aplica cada regla SI-ENTONCES al vehículo y suma los puntos.
    Devuelve el puntaje normalizado a 100 y el detalle regla por regla
    (esto alimenta el nodo 16 "Explicación del resultado").
    """
    puntaje_obtenido = 0
    peso_total_aplicable = 0
    detalle = []

    for clave, regla in REGLAS:
        puntos, explicacion = regla(vehiculo, respuestas)
        nombre_regla = regla.__doc__.strip().splitlines()[0]

        if puntos is None:
            # La regla no aplicó (p. ej. marca no seleccionada): no cuenta
            # ni suma ni resta, simplemente se saca del total posible.
            continue

        peso_total_aplicable += PESOS[clave]
        puntaje_obtenido += puntos
        detalle.append({"regla": nombre_regla, "puntos": round(puntos, 1), "razon": explicacion})

    # Normalización: si alguna regla no aplicó (ej. sin marca preferida),
    # reescalamos sobre 100 para que todos los vehículos sean comparables
    # entre sí sin castigar al usuario por no dar esa preferencia.
    puntaje_normalizado = (puntaje_obtenido / peso_total_aplicable) * 100 if peso_total_aplicable else 0
    return round(puntaje_normalizado, 1), detalle


def motor_inferencia(df_vehiculos: pd.DataFrame, respuestas: dict, top_n: int = 3):
    """
    Recorre toda la base de hechos (cada fila = un vehículo), le calcula
    puntaje, ordena de mayor a menor y devuelve el Top N con su explicación.
    """
    candidatos = []
    for _, vehiculo in df_vehiculos.iterrows():
        puntaje, detalle = calcular_puntaje(vehiculo, respuestas)
        candidatos.append({"vehiculo": vehiculo, "puntaje": puntaje, "detalle": detalle})

    candidatos.sort(key=lambda c: c["puntaje"], reverse=True)
    return candidatos[:top_n]


# =============================================================================
# 5) INTERFAZ DE PREGUNTAS (recorre el mapa de nodos 2 al 10 de tu diagrama)
# =============================================================================
def preguntar(mensaje, opciones):
    """Función auxiliar: muestra opciones numeradas y valida la respuesta."""
    print(f"\n{mensaje}")
    for i, opcion in enumerate(opciones, start=1):
        print(f"  {i}. {opcion}")
    while True:
        try:
            eleccion = int(input("Seleccione una opción (número): "))
            if 1 <= eleccion <= len(opciones):
                return opciones[eleccion - 1]
        except ValueError:
            pass
        print("Opción inválida, intente de nuevo.")


def recolectar_respuestas(df_vehiculos: pd.DataFrame) -> dict:
    """Guion de preguntas: un nodo del diagrama = una pregunta acá."""
    respuestas = {}
    respuestas["presupuesto"] = preguntar("¿Cuál es su presupuesto?", ORDEN_PRESUPUESTO)
    respuestas["tipo_vehiculo"] = preguntar(
        "¿Qué tipo de vehículo desea?", sorted(df_vehiculos["tipo_vehiculo"].unique())
    )
    respuestas["proposito"] = preguntar(
        "¿Cuál es el propósito principal?", sorted(df_vehiculos["proposito_principal"].unique())
    )
    respuestas["tecnologia"] = preguntar(
        "¿Qué tecnología prefiere?", sorted(df_vehiculos["tecnologia"].unique())
    )
    respuestas["terreno"] = preguntar(
        "¿Qué terreno recorrerá?", sorted(df_vehiculos["terreno"].unique())
    )
    respuestas["pasajeros"] = int(
        preguntar("¿Cuántos pasajeros necesita?", sorted(df_vehiculos["pasajeros"].unique().astype(str)))
    )
    respuestas["transmision"] = preguntar(
        "¿Qué transmisión prefiere?", sorted(df_vehiculos["transmision"].unique())
    )
    respuestas["consumo"] = preguntar("¿Qué nivel de consumo desea?", ORDEN_CONSUMO)

    tiene_marca = preguntar("¿Tiene una marca preferida?", ["Sí", "No"])
    if tiene_marca == "Sí":
        respuestas["marca"] = preguntar("Seleccione la marca", sorted(df_vehiculos["marca"].unique()))
    else:
        respuestas["marca"] = None

    return respuestas


# =============================================================================
# 6) SALIDA: Top 3 + explicación (nodos 15 y 16 del diagrama)
# =============================================================================
def mostrar_resultado(top_candidatos):
    print("\n" + "=" * 60)
    print("TOP 3 RECOMENDACIONES")
    print("=" * 60)
    for posicion, candidato in enumerate(top_candidatos, start=1):
        v = candidato["vehiculo"]
        print(f"\n#{posicion} - {v['marca']} {v['modelo']}  |  Puntaje: {candidato['puntaje']}/100")
        print(f"    Precio aprox: ${v['precio']}M  |  {v['tipo_vehiculo']} | {v['tecnologia']} | {v['transmision']}")
        print("    Explicación:")
        for item in candidato["detalle"]:
            if item["puntos"] > 0:
                print(f"      - {item['razon']}  (+{item['puntos']} pts)")


# =============================================================================
# 7) PUNTO DE ENTRADA
# =============================================================================
if __name__ == "__main__":
    df_vehiculos = cargar_vehiculos()

    while True:
        respuestas_usuario = recolectar_respuestas(df_vehiculos)
        top3 = motor_inferencia(df_vehiculos, respuestas_usuario, top_n=3)
        mostrar_resultado(top3)

        # Nodo extra al final del flujo: en vez de terminar seco después del
        # Top 3, le preguntamos al usuario si quiere correr el motor otra vez
        # (por ejemplo, para comparar con otro presupuesto o propósito distinto)
        # o si prefiere salir. "while True" + "break" es el patrón estándar en
        # Python para repetir un bloque hasta que una condición lo corte.
        continuar = preguntar("¿Quieres que te recomiende otro vehículo?", ["Sí", "No"])
        if continuar == "No":
            print("\nFue un placer recomendarte tu vehículo. ¡Hasta pronto!")
            break