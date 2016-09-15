from flask import render_template, session, request, redirect, url_for, current_app, jsonify, abort
from . import uikit
import datetime
from app.classes import stringFunctions
from app.classes.errorHandler import ApiErrorBaseClass, ResourceDoesNotExist, ResourceDoesNotExist2, CustomErrorMessage
from app.classes.decorators.limiter import limit
from app.classes.decorators.timing import add_timing_information
from app.classes.cache import cache

@uikit.route( "/" )
@cache.memoize( timeout = 30 )
def uikit_index():
	return render_template( "uikit_index.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/2" )
@cache.memoize( timeout = 30 )
def uikit_index2():
	return render_template( "uikit_index2.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/about" )
@cache.memoize( timeout = 30 )
def uikit_about():
	return render_template( "uikit_about.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/accordion" )
@cache.memoize( timeout = 30 )
def uikit_accordion():
	return render_template( "uikit_accordion.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/alerts" )
@cache.memoize( timeout = 30 )
def uikit_alerts():
	return render_template( "uikit_alerts.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/animations" )
@cache.memoize( timeout = 30 )
def uikit_animations():
	return render_template( "uikit_animations.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/articles" )
@cache.memoize( timeout = 30 )
def uikit_articles():
	return render_template( "uikit_articles.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/autocomplete" )
@cache.memoize( timeout = 30 )
def uikit_autocomplete():
	return render_template( "uikit_autocomplete.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/badges" )
@cache.memoize( timeout = 30 )
def uikit_badges():
	return render_template( "uikit_badges.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/base" )
@cache.memoize( timeout = 30 )
def uikit_base():
	return render_template( "uikit_base.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/blocks" )
@cache.memoize( timeout = 30 )
def uikit_blocks():
	return render_template( "uikit_blocks.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/breadcrumb" )
@cache.memoize( timeout = 30 )
def uikit_breadcrumb():
	return render_template( "uikit_breadcrumb.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/buttons" )
@cache.memoize( timeout = 30 )
def uikit_buttons():
	return render_template( "uikit_buttons.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/close" )
@cache.memoize( timeout = 30 )
def uikit_close():
	return render_template( "uikit_close.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/column" )
@cache.memoize( timeout = 30 )
def uikit_column():
	return render_template( "uikit_column.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/comments" )
@cache.memoize( timeout = 30 )
def uikit_comments():
	return render_template( "uikit_comments.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/contrast" )
@cache.memoize( timeout = 30 )
def uikit_contrast():
	return render_template( "uikit_contrast.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/cover" )
@cache.memoize( timeout = 30 )
def uikit_cover():
	return render_template( "uikit_cover.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/custom" )
@cache.memoize( timeout = 30 )
def uikit_custom():
	return render_template( "uikit_custom.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/datepicker" )
@cache.memoize( timeout = 30 )
def uikit_datepicker():
	return render_template( "uikit_datepicker.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/descriptionlist" )
@cache.memoize( timeout = 30 )
def uikit_descriptionlist():
	return render_template( "uikit_descriptionlist.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/dotnav" )
@cache.memoize( timeout = 30 )
def uikit_dotnav():
	return render_template( "uikit_dotnav.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/dropdowns" )
@cache.memoize( timeout = 30 )
def uikit_dropdowns():
	return render_template( "uikit_dropdowns.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/dynamicgrid" )
@cache.memoize( timeout = 30 )
def uikit_dynamicgrid():
	return render_template( "uikit_dynamicgrid.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/dynamicpagination" )
@cache.memoize( timeout = 30 )
def uikit_dynamicpagination():
	return render_template( "uikit_dynamicpagination.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/flex" )
@cache.memoize( timeout = 30 )
def uikit_flex():
	return render_template( "uikit_flex.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/forms" )
@cache.memoize( timeout = 30 )
def uikit_forms():
	return render_template( "uikit_forms.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/formadvanced" )
@cache.memoize( timeout = 30 )
def uikit_formadvanced():
	return render_template( "uikit_formadvanced.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/formfile" )
@cache.memoize( timeout = 30 )
def uikit_formfile():
	return render_template( "uikit_formfile.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/formpassword" )
@cache.memoize( timeout = 30 )
def uikit_formpassword():
	return render_template( "uikit_formpassword.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/formselect" )
@cache.memoize( timeout = 30 )
def uikit_formselect():
	return render_template( "uikit_formselect.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/grid" )
@cache.memoize( timeout = 30 )
def uikit_grid():
	return render_template( "uikit_grid.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/htmleditor" )
@cache.memoize( timeout = 30 )
def uikit_htmleditor():
	return render_template( "uikit_htmleditor.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/icons" )
@cache.memoize( timeout = 30 )
def uikit_icons():
	return render_template( "uikit_icons.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/lists" )
@cache.memoize( timeout = 30 )
def uikit_lists():
	return render_template( "uikit_lists.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/lightbox" )
@cache.memoize( timeout = 30 )
def uikit_lightbox():
	return render_template( "uikit_lightbox.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/modal" )
@cache.memoize( timeout = 30 )
def uikit_modal():
	return render_template( "uikit_modal.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/nav" )
@cache.memoize( timeout = 30 )
def uikit_nav():
	return render_template( "uikit_nav.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/navbar" )
@cache.memoize( timeout = 30 )
def uikit_navbar():
	return render_template( "uikit_navbar.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/nestable" )
@cache.memoize( timeout = 30 )
def uikit_nestable():
	return render_template( "uikit_nestable.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/notify" )
@cache.memoize( timeout = 30 )
def uikit_notify():
	return render_template( "uikit_notify.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/offcanvas" )
@cache.memoize( timeout = 30 )
def uikit_offcanvas():
	return render_template( "uikit_offcanvas.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/overlays" )
@cache.memoize( timeout = 30 )
def uikit_overlays():
	return render_template( "uikit_overlay.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/pagination" )
@cache.memoize( timeout = 30 )
def uikit_pagination():
	return render_template( "uikit_pagination.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/panels" )
@cache.memoize( timeout = 30 )
def uikit_panels():
	return render_template( "uikit_panels.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/parallax" )
@cache.memoize( timeout = 30 )
def uikit_parallax():
	return render_template( "uikit_parallax.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/placeholder" )
@cache.memoize( timeout = 30 )
def uikit_placeholder():
	return render_template( "uikit_placeholder.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/progress" )
@cache.memoize( timeout = 30 )
def uikit_progress():
	return render_template( "uikit_progress.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/scroll" )
@cache.memoize( timeout = 30 )
def uikit_scroll():
	return render_template( "uikit_scroll.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/search" )
@cache.memoize( timeout = 30 )
def uikit_search():
	return render_template( "uikit_search.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/slider" )
@cache.memoize( timeout = 30 )
def uikit_slider():
	return render_template( "uikit_slider.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/slidenav" )
@cache.memoize( timeout = 30 )
def uikit_slidenav():
	return render_template( "uikit_slidenav.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/slideset" )
@cache.memoize( timeout = 30 )
def uikit_slideset():
	return render_template( "uikit_slideset.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/slideshow" )
@cache.memoize( timeout = 30 )
def uikit_slideshow():
	return render_template( "uikit_slideshow.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/smoothscroll" )
@cache.memoize( timeout = 30 )
def uikit_smoothscroll():
	return render_template( "uikit_smoothscroll.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/sortable" )
@cache.memoize( timeout = 30 )
def uikit_sortable():
	return render_template( "uikit_sortable.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/sticky" )
@cache.memoize( timeout = 30 )
def uikit_sticky():
	return render_template( "uikit_sticky.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/subnav" )
@cache.memoize( timeout = 30 )
def uikit_subnav():
	return render_template( "uikit_subnav.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/switcher" )
@cache.memoize( timeout = 30 )
def uikit_switcher():
	return render_template( "uikit_switcher.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/tables" )
@cache.memoize( timeout = 30 )
def uikit_tables():
	return render_template( "uikit_tables.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/tabs" )
@cache.memoize( timeout = 30 )
def uikit_tabs():
	return render_template( "uikit_tabs.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/text" )
@cache.memoize( timeout = 30 )
def uikit_text():
	return render_template( "uikit_text.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/timepicker" )
@cache.memoize( timeout = 30 )
def uikit_timepicker():
	return render_template( "uikit_timepicker.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/toggle" )
@cache.memoize( timeout = 30 )
def uikit_toggle():
	return render_template( "uikit_toggle.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/tooltip" )
@cache.memoize( timeout = 30 )
def uikit_tooltip():
	return render_template( "uikit_tooltip.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/thumbnails" )
@cache.memoize( timeout = 30 )
def uikit_thumbnail():
	return render_template( "uikit_thumbnail.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/thumbnails2" )
@cache.memoize( timeout = 30 )
def uikit_thumbnails2():
	return render_template( "uikit_thumbnails2.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/upload" )
@cache.memoize( timeout = 30 )
def uikit_upload():
	return render_template( "uikit_upload.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@uikit.route( "/utility" )
@cache.memoize( timeout = 30 )
def uikit_utility():
	return render_template( "uikit_utility.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )
