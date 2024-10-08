# Software de información financiera
Esta aplicación de escritorio facilita la obtención de información financiera de empresas cotizantes en la bolsa de valores de EEUU a través de la API de la compañía Alpha Vantage. 
Los datos son devueltos en formato .xlsx (Excel) para ser posteriormente procesados ya sea por SGBD o plataformas de inteligencia empresarial como Power BI. Actualmente cuenta con **dos servicios y sus respectivas opciones**:

_Fundamentals_: información contable y financiera de la compañía 
- Overview: información general de la compañía
- Income statement: estados de resultados de los últimos 5 períodos
- Balance sheet: balances de los últimos 5 períodos
- Cash flow: estado financiero donde se muestran los flujos de fondos
- Earnings: datos sobre la fecha de presentación de resultados, ganancias por acción presentadas, EPS esperada y el nivel de "sorpresa" absoluta y relativa.
- Dividends: información sobre el pago de dividendos por fecha de la compañía.
- Splits: historial de 'splits' realizados por la compañía.
- ETF Profile: perfil y composición de los diferentes ETF

_Time Series_: series de tiempo de los precios de apertura, cierre, máximo, mínimo junto con el volumen operado (incluye opción de ajustados)
- Intradiario
- Diario
- Diario ajustado
- Semanal
- Semanal ajustado
- Mensual
- Mensual ajustado
- Global quote (último precio y volumen)

## Cómo utilizarlo
Se debe reclamar la free API key en [el servicio de Alpha Vantage](https://www.alphavantage.co/support/#api-key). Una vez obtenida, podemos ejecutar el script de Python que abrirá una aplicación de escritorio. Allí nos solicitará los siguientes datos:
1. Servicio a utilizar (información requerida)
2. Ticker (acción o ETF)
3. Intervalo (obligatorio solo para series de tiempo intradiario)
4. API key obtenida
   
## Restricciones a su uso
De acuerdo con la documentación del servicio de Alpha Vantage, en su versión gratuita se permiten hasta 25 API calls por día para obtener la información requerida. 
