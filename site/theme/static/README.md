# Rebuilding the theme

Get node.js + npm.

Install less with npm:

    npm install -l less grunt-cli grunt-contrib-less grunt-contrib-watch

Edit `libertymusicstore.less` and related theme files.

Rebuilding the theme CSS:

    node_modules/grunt-cli/bin/grunt less

Rebuiding the theme production deployment (minified CSS):

    node_modules/grunt-cli/bin/grunt production

# Live editing of LESS

Then start `grunt` in watch mode. This will recompile CSS when LESS files are edited, either in the web browser or your text editor:

     node_modules/grunt-cli/bin/grunt watch
