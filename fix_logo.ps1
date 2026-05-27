$files = @(
  'index.html',
  'criminal-law.html',
  'civil-law.html',
  'constitutional-law.html',
  'family-law.html',
  'ndps-matters.html',
  'money-laundering.html',
  'dispute-resolution.html',
  'non-litigation.html',
  'service-matters.html',
  'contact.html',
  'careers.html'
)

$basePath = 'c:\Users\TEJAL CHAVAN\Desktop\sijjumallli\sijjumallli'

foreach ($f in $files) {
  $path = Join-Path $basePath $f
  $content = [System.IO.File]::ReadAllText($path)

  # Add cache-busting to logo.png references
  $content = $content.Replace('src="logo.png"', 'src="logo.png?v=2"')

  [System.IO.File]::WriteAllText($path, $content)
  Write-Host "Cache-busted logo in $f"
}
