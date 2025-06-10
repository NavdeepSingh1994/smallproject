<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:template match="/assets">
    <html>
    <head>
      <title>DAM Asset Übersicht</title>
      <style>
        body { font-family: sans-serif; background: #f8f8f8; padding: 20px; }
        .asset { background: #fff; border: 1px solid #ccc; padding: 15px; margin: 10px 0; border-radius: 6px; }
        img { max-width: 300px; display: block; margin-bottom: 10px; border-radius: 4px; }
        a { text-decoration: none; color: #0066cc; font-weight: bold; }
      </style>
    </head>
    <body>
      <h1>📦 Asset-Vorschau (XML mit Stylesheet)</h1>
      <xsl:for-each select="asset">
        <div class="asset">
          <h2><xsl:value-of select="name"/></h2>
          <img>
            <xsl:attribute name="src">
              <xsl:value-of select="url"/>
            </xsl:attribute>
          </img>
          <p>
            <a>
              <xsl:attribute name="href">
                <xsl:value-of select="link"/>
              </xsl:attribute>
              <xsl:value-of select="cta"/>
            </a>
          </p>
        </div>
      </xsl:for-each>
    </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
