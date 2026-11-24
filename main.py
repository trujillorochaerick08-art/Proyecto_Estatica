from clases.fuerza import Fuerza
from clases.sistema_estatico import SistemaEstatico

MENU = '''\n=== CALCULADORA DE ESTÁTICA (PLANO XZ) ===
1. Registrar fuerza
2. Calcular componentes
3. Calcular momentos
4. Calcular resultante
5. Verificar equilibrio
6. Mostrar fuerzas registradas
7. Eliminar fuerza
8. Salir'''

def main():
    sistema = SistemaEstatico()
    while True:
        print(MENU)
        opcion = input('Opción: ').strip()
        try:
            if opcion == '1':
                f = Fuerza(float(input('Magnitud (N): ')), float(input('Ángulo desde +X hacia +Z (grados): ')), float(input('Posición X (m): ')), float(input('Posición Z (m): ')))
                sistema.agregar(f)
                print('Fuerza registrada.')
            elif opcion == '8':
                print('Fin del programa.')
                break
            elif opcion not in ('2','3','4','5','6','7'):
                print('Opción inválida.')
            elif not sistema.fuerzas:
                print('Primero registra una fuerza.')
            elif opcion == '2':
                for i, f in enumerate(sistema.fuerzas, 1):
                    fx, fz = f.componentes()
                    print(f'F{i}: Fx={fx:.2f} N, Fz={fz:.2f} N')
            elif opcion == '3':
                for i, f in enumerate(sistema.fuerzas, 1):
                    print(f'F{i}: My={f.momento():.2f} N·m')
                print(f'Momento total My={sistema.momento_total():.2f} N·m')
            elif opcion == '4':
                sx, sz, r = sistema.resultante()
                print(f'Suma Fx={sx:.2f} N, Suma Fz={sz:.2f} N, R={r:.2f} N')
            elif opcion == '5':
                print('En equilibrio' if sistema.equilibrio() else 'No está en equilibrio')
            elif opcion == '6':
                for i, f in enumerate(sistema.fuerzas, 1):
                    print(f'{i}: {f.magnitud} N, {f.angulo}°, posición ({f.x}, {f.z}) m')
            elif opcion == '7':
                sistema.eliminar(int(input('Número de fuerza: ')))
                print('Fuerza eliminada.')
        except ValueError as error:
            print(f'Entrada inválida: {error}')

if __name__ == '__main__':
    main()
