class ApplicationController < ActionController::Base
  # Prevent CSRF attacks by raising an exception.
  # For APIs, you may want to use :null_session instead.
  protect_from_forgery with: :exception

  def hello
  	render html: "¡Hola, mundo!"
  end

  def goodbye
  	render html: "Goodbye World!"
  end
end