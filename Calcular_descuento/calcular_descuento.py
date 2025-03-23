def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Función para calcular el descuento en una compra.

    Args:
    monto_total (float): El monto total de la compra.
    porcentaje_descuento (float): El porcentaje de descuento a aplicar (default 10%).

    Returns:
    tuple: El monto del descuento y el monto final a pagar después del descuento.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    monto_final = monto_total - descuento
    return descuento, monto_final
def main():
    # Primera llamada, usando el descuento predeterminado (10%)
    monto1 = 1500.0  # Monto total de la compra
    descuento1, monto_final1 = calcular_descuento(monto1)
    print(f"Compra 1: Monto Total: ${monto1}, Descuento: ${descuento1}, Monto Final a Pagar: ${monto_final1}")

    # Segunda llamada, especificando el descuento (15%)
    monto2 = 2000.0  # Monto total de la compra
    porcentaje_descuento2 = 15  # 15% de descuento
    descuento2, monto_final2 = calcular_descuento(monto2, porcentaje_descuento2)
    print(f"Compra 2: Monto Total: ${monto2}, Descuento: ${descuento2}, Monto Final a Pagar: ${monto_final2}")

if __name__ == "__main__":
    main()
