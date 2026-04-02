# fix-encoding.ps1 - Fix broken UTF-8 double-encoding in all HTML files
# Uses byte-level replacements to avoid encoding issues in the script itself

$files = Get-ChildItem -Recurse -Filter "*.html" | Where-Object { -not $_.PSIsContainer }

foreach ($file in $files) {
    try {
        $content = [System.IO.File]::ReadAllText($file.FullName, [System.Text.Encoding]::UTF8)
        $fixed = $content

        # Em dash (—) - various broken forms
        $fixed = $fixed.Replace([System.Text.Encoding]::UTF8.GetString([byte[]](0xC3,0xA2,0xC2,0x80,0xC2,0x94)), [char]0x2014)
        $fixed = $fixed.Replace([System.Text.Encoding]::UTF8.GetString([byte[]](0xE2,0x80,0x94)), [char]0x2014)
        # En dash (-)
        $fixed = $fixed.Replace([System.Text.Encoding]::UTF8.GetString([byte[]](0xC3,0xA2,0xC2,0x80,0xC2,0x93)), [char]0x2013)
        $fixed = $fixed.Replace([System.Text.Encoding]::UTF8.GetString([byte[]](0xE2,0x80,0x93)), [char]0x2013)
        # Right single quote (')
        $fixed = $fixed.Replace([System.Text.Encoding]::UTF8.GetString([byte[]](0xC3,0xA2,0xC2,0x80,0xC2,0x99)), [char]0x2019)
        $fixed = $fixed.Replace([System.Text.Encoding]::UTF8.GetString([byte[]](0xE2,0x80,0x99)), [char]0x2019)
        # Left single quote (')
        $fixed = $fixed.Replace([System.Text.Encoding]::UTF8.GetString([byte[]](0xC3,0xA2,0xC2,0x80,0xC2,0x98)), [char]0x2018)
        $fixed = $fixed.Replace([System.Text.Encoding]::UTF8.GetString([byte[]](0xE2,0x80,0x98)), [char]0x2018)
        # Left double quote (")
        $fixed = $fixed.Replace([System.Text.Encoding]::UTF8.GetString([byte[]](0xC3,0xA2,0xC2,0x80,0xC5,0x93)), [char]0x201C)
        $fixed = $fixed.Replace([System.Text.Encoding]::UTF8.GetString([byte[]](0xE2,0x80,0x9C)), [char]0x201C)
        # Right double quote (")
        $fixed = $fixed.Replace([System.Text.Encoding]::UTF8.GetString([byte[]](0xC3,0xA2,0xC2,0x80,0xC2,0x9D)), [char]0x201D)
        $fixed = $fixed.Replace([System.Text.Encoding]::UTF8.GetString([byte[]](0xE2,0x80,0x9D)), [char]0x201D)
        # Ellipsis (...)
        $fixed = $fixed.Replace([System.Text.Encoding]::UTF8.GetString([byte[]](0xC3,0xA2,0xC2,0x80,0xC2,0xA6)), '...')
        $fixed = $fixed.Replace([System.Text.Encoding]::UTF8.GetString([byte[]](0xE2,0x80,0xA6)), '...')
        # Non-breaking space / stray Â
        $fixed = $fixed.Replace([System.Text.Encoding]::UTF8.GetString([byte[]](0xC3,0x82,0xC2,0xA0)), ' ')
        $fixed = $fixed.Replace([System.Text.Encoding]::UTF8.GetString([byte[]](0xC3,0x82)), '')
        $fixed = $fixed.Replace([System.Text.Encoding]::UTF8.GetString([byte[]](0xC2,0xA0)), ' ')

        if ($fixed -ne $content) {
            [System.IO.File]::WriteAllText($file.FullName, $fixed, [System.Text.Encoding]::UTF8)
            Write-Host "Fixed: $($file.FullName.Replace((Get-Location).Path + '\', ''))"
        } else {
            Write-Host "Clean: $($file.Name)"
        }
    } catch {
        Write-Host "Skipped (locked): $($file.Name)"
    }
}

Write-Host ""
Write-Host "Done! Now run: git add . && git commit -m 'Fix encoding' && git push"
