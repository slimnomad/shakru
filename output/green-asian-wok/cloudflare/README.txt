Green Asian Wok — Cloudflare Workers upload package

Extract the ZIP and upload its CONTENTS to your GitHub repository.
The repository root must contain wrangler.jsonc and the public/ folder.
Keep the files in public/ together so image, font, CSS and JavaScript paths work.

Cloudflare setup fields:
  Project name: shakru
  Build command: leave empty
  Deploy command: npx wrangler deploy
  Preview command: npx wrangler preview
  Enable Preview builds: enabled
  Root directory, if shown: repository root

This is the original plain HTML/CSS/JavaScript website. No build is required.
Cloudflare serves only files inside public/. No server script is needed.
If you rename the Cloudflare project, update "name" in wrangler.jsonc to match.

After deploying:
  Workers & Pages > shakru > Settings > Domains & Routes > Add > Custom Domain
  Enter your domain, without https:// or a path, and select Add Custom Domain.
  Add the www hostname separately if you want both domain forms to work.
  The domain must be active in your Cloudflare account. If it is not already
  there, add it to Cloudflare and complete its nameserver setup first.
  Cloudflare creates the DNS record and TLS certificate for the custom domain.

Documentation:
  https://developers.cloudflare.com/workers/static-assets/binding/
  https://developers.cloudflare.com/workers/ci-cd/builds/configuration/
  https://developers.cloudflare.com/workers/configuration/routing/custom-domains/

This package has not been deployed. It contains no domain-specific configuration.
Menu/business facts and the food asset attribution are documented in the full
project README.md. The food images are illustrative, not verified restaurant
photographs. Ordering opens the existing official provider; selections must be
made again there. The static files are the same tested website previously supplied.
