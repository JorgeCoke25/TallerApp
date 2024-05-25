import sys,traceback
try:
  import tkinter as tk
  from tkinter import messagebox
  import requests
  from weasyprint import HTML
  import os
  from datetime import datetime
  import locale
  from PIL import Image, ImageTk
  import re




  def generar_pdf_desde_html(html_content, output_path):
      HTML(string=html_content, base_url=".").write_pdf(output_path)

  def abrir_pdf(nombre_archivo):
      try:
        directorio_actual = os.getcwd()
        ruta_pdf = os.path.join(directorio_actual, "Presupuestos", nombre_archivo)
        os.startfile(ruta_pdf)
      except Exception as e:
        print("Error al abrir el archivo PDF:", e)


  def obtener_fecha_actual():
      fecha_actual = datetime.now()
      fecha_formateada = fecha_actual.strftime('%d/%m/%Y')
      return fecha_formateada

  def peticion_patente(patente):
      url_base = 'https://api.boostr.cl/vehicle/'
      headers = {
          'x-api-key': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnQiOiJqb3JnZV9iYXJyaW9zIiwicGxhbiI6ImZyZWUiLCJhZGRvbnMiOiIiLCJyYXRlIjoiNXgxMCIsImlhdCI6MTcwNzQ1MTgwOSwiZXhwIjoxNzM5MDA5NDA5fQ.AOBf8ZqvmQFJrnpflOerYi85lyEZfHq840j-AOmp0aw'
      }
      response = requests.get(url_base + patente + '.json', headers=headers)
      return response.json()['data']

  def format_price(entry):
      current_text = entry.get()
      cleaned_text = ''.join(filter(str.isdigit, current_text))
      formatted_text = "{:,}".format(int(cleaned_text)).replace(",", ".")
      entry.delete(0, tk.END)
      entry.insert(0, formatted_text)
      entry.raw_value = int(cleaned_text)


  def mostrar_ventana_datos(n_servicios, n_piezas):
      ventana_datos = tk.Toplevel(root)
      ventana_datos.title("Ingrese datos para servicios y piezas")


      canvas = tk.Canvas(ventana_datos)
      canvas.pack(side="left", fill="both", expand=True)

      scroll_y = tk.Scrollbar(ventana_datos, orient="vertical", command=canvas.yview)
      scroll_y.pack(side="right", fill="y")
      canvas.configure(yscrollcommand=scroll_y.set)

      frame = tk.Frame(canvas)
      canvas.create_window((0, 0), window=frame, anchor='nw')

      label_servicios = tk.Label(frame, text="Servicios",font=("Arial", 12, "bold"))
      label_servicios.grid(row=0, column=3, columnspan=2, padx=5, pady=5)

      for i in range(n_servicios):
          label_descripcion = tk.Label(frame, text=f"Descripción servicio {i + 1}:")
          label_descripcion.grid(row=i + 1, column=2, columnspan=1,padx=5, pady=5, sticky="w")
          entry_descripcion = tk.Entry(frame, name=f"entry_descripcion_{i + 1}")
          entry_descripcion.grid(row=i + 1, column=3, columnspan=1,padx=5, pady=5)

          label_valor = tk.Label(frame, text=f"Valor servicio {i + 1}:")
          label_valor.grid(row=i + 1, column=4, columnspan=1,padx=5, pady=5, sticky="w")
          entry_valor = tk.Entry(frame, name=f"entry_valor_{i + 1}")
          entry_valor.grid(row=i + 1, column=5, columnspan=1,padx=5, pady=5)
          entry_valor.bind("<KeyRelease>", lambda event, entry=entry_valor: format_price(entry))

      label_piezas = tk.Label(frame, text="Piezas",font=("Arial", 12, "bold"))
      label_piezas.grid(row=n_servicios + 2, column=3, columnspan=2,padx=5, pady=5)

      for i in range(n_piezas):
          label_descripcion = tk.Label(frame, text=f"Descripción pieza {i + 1}:")
          label_descripcion.grid(row=n_servicios + i + 3, column=1, padx=5, pady=5, sticky="w")
          entry_descripcion = tk.Entry(frame, name=f"entry_descripcion_{n_servicios + i + 1}")
          entry_descripcion.grid(row=n_servicios + i + 3, column=2, padx=5, pady=5)

          label_valor = tk.Label(frame, text=f"Valor pieza {i + 1}:")
          label_valor.grid(row=n_servicios + i + 3, column=3, padx=5, pady=5, sticky="w")
          entry_valor = tk.Entry(frame, name=f"entry_valor_{n_servicios + i + 1}")
          entry_valor.grid(row=n_servicios + i + 3, column=4, padx=5, pady=5)
          entry_valor.bind("<KeyRelease>", lambda event, entry=entry_valor: format_price(entry))

          label_cantidad = tk.Label(frame, text=f"Cantidad de piezas {i + 1}:")
          label_cantidad.grid(row=n_servicios + i + 3, column=5, padx=5, pady=5, sticky="w")
          entry_cantidad = tk.Entry(frame, name=f"entry_cantidad_{i + 1}")
          entry_cantidad.grid(row=n_servicios + i + 3, column=6, padx=5, pady=5)

      label_patente = tk.Label(frame, text="Patente del auto:",font=("Arial", 12, "bold"))
      label_patente.grid(row=n_servicios + n_piezas + 4, column=3,columnspan=1, padx=5, pady=5)
      entry_patente = tk.Entry(frame, name="entry_patente")
      entry_patente.grid(row=n_servicios + n_piezas + 5, column=3,columnspan=1, padx=5, pady=5)

      label_rut = tk.Label(frame, text="Rut:",font=("Arial", 12, "bold"))
      label_rut.grid(row=n_servicios + n_piezas + 4, column=4,columnspan=1, padx=5, pady=5)
      entry_rut = tk.Entry(frame, name="entry_rut")
      entry_rut.grid(row=n_servicios + n_piezas + 5, column=4,columnspan=1,padx=5, pady=5)

      label_nombre = tk.Label(frame, text="Nombre:",font=("Arial", 12, "bold"))
      label_nombre.grid(row=n_servicios + n_piezas + 6, column=3,columnspan=1,padx=5, pady=5)
      entry_nombre = tk.Entry(frame, name="entry_nombre")
      entry_nombre.grid(row=n_servicios + n_piezas + 7, column=3,columnspan=1,padx=5, pady=5)
      
      label_np = tk.Label(frame, text="Numero de presupuesto:",font=("Arial", 12, "bold"))
      label_np.grid(row=n_servicios + n_piezas + 6, column=4,columnspan=1, padx=5, pady=5)
      entry_np = tk.Entry(frame, name="entry_np")
      entry_np.grid(row=n_servicios + n_piezas + 7, column=4,columnspan=1,padx=5, pady=5)

      button_generar_pdf = tk.Button(frame, text="Generar PDF", command=lambda: generar_pdf(frame, n_servicios, n_piezas))
      button_generar_pdf.grid(row=n_servicios + n_piezas + 8,column=3,columnspan=2, padx=5, pady=5)

      frame.update_idletasks()
      canvas.config(scrollregion=canvas.bbox("all"))

      ventana_datos.update_idletasks()
      ventana_datos.geometry(f"{frame.winfo_reqwidth()+20}x{frame.winfo_reqheight()}")

  def obtener_datos():
      n_servicios = int(var1.get())
      n_piezas = int(var2.get())
      mostrar_ventana_datos(n_servicios, n_piezas)

  def obtener_datos_ventana(ventana_datos, n_servicios, n_piezas):
      patente = ventana_datos.children['entry_patente'].get()
      rut = ventana_datos.children['entry_rut'].get()
      nombre = ventana_datos.children['entry_nombre'].get()
      np = ventana_datos.children['entry_np'].get()
      
      valores_servicios = []
      for i in range(n_servicios):
          descripcion_servicio = ventana_datos.children[f"entry_descripcion_{i + 1}"].get()
          valor_servicio = ventana_datos.children[f"entry_valor_{i + 1}"].raw_value
          valores_servicios.append((descripcion_servicio, valor_servicio))

      valores_piezas = []
      for i in range(n_piezas):
          descripcion_pieza = ventana_datos.children[f"entry_descripcion_{n_servicios + i + 1}"].get()
          valor_pieza = ventana_datos.children[f"entry_valor_{n_servicios + i + 1}"].raw_value
          cantidad_piezas = ventana_datos.children[f"entry_cantidad_{i + 1}"].get()

          valores_piezas.append((descripcion_pieza, valor_pieza, cantidad_piezas))
      return np,patente,rut,nombre, valores_servicios, valores_piezas


  def generar_pdf(ventana_datos, n_servicios, n_piezas):
      np,patente,rut,nombre, valores_servicios, valores_piezas = obtener_datos_ventana(ventana_datos, n_servicios, n_piezas)
      locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')
      fecha = datetime.now()
      try:
          r = peticion_patente(patente)
          html_content = """
              <!DOCTYPE html>
                  <html lang="es">
                  <head>
                  <meta charset="UTF-8">
                  <meta name="viewport" content="width=device-width, initial-scale=1.0">
                  <title>planilla presupuesto</title>
                  <style>
                    @page {
                      size: letter;
                      margin: 15mm;
                    }
                  
                    body {
                      font-family: Arial, sans-serif;
                      font-size: 11pt;
                      line-height: 0.4;
                      padding: 0;
                    }
                  
                    table {
                      width: 100%; 
                      margin-bottom: 5mm; 
                      margin-top: 5mm;
                      border-collapse: collapse; 
                    }
                  
                    .table p {
                      margin-top: 0; 
                      margin-bottom: 0; 
                    }
                    th, td {
                      border: 1px solid black; 
                      padding: 5px; 
                      text-align: left;
                    }
                    .tabla-derecha {
                      float: right;
                      margin-left: 10px;
                      clear: left;
                      width: 70%;
                    }
                    .tabla-derecha p {
                      margin-top: 0;
                      margin-bottom: 0;
                    }
                    h2 {
                      font-size: 20px;
                      margin-bottom: 20px;
                      text-align: center;
                    }
                    .clear {
                      clear: both;
                    }
                    .auto-height {
                        height: auto;
                        max-height: 100px; /* Establece una altura máxima opcional para evitar que la celda se expanda demasiado */
                        overflow-y: auto; /* Agrega una barra de desplazamiento vertical si el contenido excede la altura máxima */
                    }
                  </style>
                  </head>
                  <body>
                  <div>
                    <img src="media/sup.png" alt="encabezado" style="width:100%;">
                    <h2>PRESUPUESTO N°"""+np+"""</h2>
                  
                    <p>Fecha:"""+fecha.strftime('%d/%m/%Y')+"""</p>
                  
                    <table>
                      <tr>
                          <th style="width: 50%;">Datos del Cliente</th>
                          <th style="width: 50%;">Datos del Vehículo</th>
                      </tr>
                      <tr>
                        <td>
                          <p>Nombre: """+nombre+"""</p>
                          <p>RUN: """+rut+"""</p>
                        </td>
                        <td>
                          <p>Patente: """+r['plate']+"""</p>
                          <p>Marca: """+r['make']+"""</p>
                          <p>Modelo: """+r['model']+"""</p>
                          <p>Año: """+str(r['year'])+"""</p>
                        </td>
                      </tr>
                    </table>
                  
                    <table>
                      <tr>
                        <th style="width:74%;">Servicio</th>
                        <th style="width:26%;text-align: center;">Precio</th>
                      </tr>
                      """
          subtotal_servicios=0
          for descripcion, precio in valores_servicios:
              html_content += f"""
                      <tr>
                          <td style="text-align: left;line-height: 1.1;">{descripcion}</td>
                          <td style="text-align: right;">$ {locale.format_string('%d',int(precio) ,grouping=True)}</td>
                      </tr>
              """
              subtotal_servicios += int(precio)
          html_content += """
                      <tr>
                          <th style="width:74%;text-align: right;">SUB-TOTAL:</th>
                          <th style="width:26%;text-align: right;">$ """+locale.format_string('%d',subtotal_servicios,grouping=True)+"""</th>
                      </tr>
                    </table>
                  
                    <table>
                      <tr>
                        <th style="width:62%;">Piezas</th>
                        <th style="width:10%;text-align: center;">Unidades</th>
                        <th style="width:14%;text-align: center;">Precio</th>
                        <th style="width:14%;text-align: center;">Total</th>
                      </tr>
          """
          subtotal_piezas = 0
          for descripcion, precio, cantidad in valores_piezas:
              precio_formateado = locale.format_string('%d',int(precio),grouping=True)
              html_content += f"""
                  <tr>
                      <td style="text-align: left;line-height: 1.1;">{descripcion}</td>
                      <td style="text-align: right;">{cantidad}</td>
                      <td style="text-align: right;">$ {precio_formateado}</td>
                      <td style="text-align: right;">$ {locale.format_string('%d',(int(precio) * int(cantidad)),grouping=True)}</td>
                  </tr>
              """
              subtotal_piezas += int(precio)*int(cantidad)
          html_content += """
                      <tr>
                          <th style="width:86%;text-align: right;" colspan="3">SUB-TOTAL:</th>
                          <th style="width:14%;text-align: right;">$ """+locale.format_string('%d',subtotal_piezas,grouping=True)+"""</th>
                      </tr>
                    </table>
                  
                    <table class="tabla-derecha">
                      <tr>
                        <th style="text-align: center;">Método de Pago</th>
                        <th style="text-align: center;">Sobrecargo</th>
                        <th style="text-align: center;">Precio Final IVA incluido</th>
                      </tr>
                      <tr>
                        <td>Efectivo o Transferencia</td>
                        <td style="text-align: right;">0%</td>
                        <td style="text-align: right;">$ """+locale.format_string('%d',(subtotal_servicios+subtotal_piezas),grouping=True)+"""</td>
                      </tr>
                      <tr>
                        <td>Débito o Crédito</td>
                        <td style="text-align: right;">3%</td>
                        <td style="text-align: right;">$ """+locale.format_string('%d',((subtotal_servicios+subtotal_piezas)*1.03),grouping=True)+"""</td>
                      </tr>
                    </table>
                    
                  
                    <div class="clear">
                    <hr style="border: 1.5mm solid  #252E58; margin: 20px 0; width: 100%;">
                      <p> <u>Datos de Transferencia:</u></p>
                      <p>SM AUTOMOTRIZ E INVERSIONES SPA</p>
                      <p>RUT: 77.574.217-8</p>
                      <p>Email: tallersmautomotriz@gmail.com</p>
                      <p>Banco: BANCO SANTANDER-BANEFE</p>
                      <p>Cuenta Corriente: 0000 8898 2045</p>
                    </div>
                    

                  </div>
                  </body>
                  </html>
          """
          pdf = "Presupuesto_"+np+".pdf"
          generar_pdf_desde_html(html_content, "Presupuestos/"+pdf)
          abrir_pdf(pdf)
      except Exception as e:
          messagebox.showerror("Error", f"Ocurrió un error al crear el PDF: {str(e)}")
          print(e)


  # Crear la ventana principal
  root = tk.Tk()
  root.title("Generador de Presupuestos")

  logo_path = "media/logoazul.png"
  logo_img = Image.open(logo_path)
  logo_img.thumbnail((150, 150))  # Ajusta el tamaño de la imagen si es necesario
  logo_photo = ImageTk.PhotoImage(logo_img)

  logo_label = tk.Label(root, image=logo_photo)
  logo_label.grid(row=0, columnspan=2, padx=10, pady=10)  
  logo_label.image = logo_photo  

  label_n_servicio = tk.Label(root, text="Numero de servicios:")
  label_n_servicio.grid(row=1, column=0, padx=30, pady=5, sticky="w")
  var1 = tk.StringVar(root)
  var1.set("1")
  entry_n_servicio = tk.OptionMenu(root, var1, *range(1,10))
  entry_n_servicio.grid(row=1, column=1,padx=5, pady=5)

  label_n_piezas = tk.Label(root, text="Numero de piezas:")
  label_n_piezas.grid(row=2, column=0, padx=30, pady=5, sticky="w")
  var2 = tk.StringVar(root)
  var2.set("1")
  entry_piezas = tk.OptionMenu(root, var2, *range(1,10))
  entry_piezas.grid(row=2, column=1,padx=5, pady=5)

  button_aceptar = tk.Button(root, text="Aceptar", command=obtener_datos)
  button_aceptar.grid(row=3, columnspan=2, padx=120, pady=20)

  root.iconbitmap('media/autorojo.ico')
  root.geometry("300x270")
  root.mainloop()
except:
  print(sys.exc_info())
  print(traceback.format_exc())
finally:
  input('Press enter to exit the program: ')