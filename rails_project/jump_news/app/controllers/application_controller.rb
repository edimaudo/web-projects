class ApplicationController < ActionController::Base
  # Prevent CSRF attacks by raising an exception.
  # For APIs, you may want to use :null_session instead.
  protect_from_forgery with: :exception
  def login(user)
  session[:user_id] = user.id
end

def current_user
  @current_user ||= User.find_by(id: session[:user_id])
end

def logout
  session.delete(:user_id)
  @current_user = nil
end

def logged_in?
  current_user.nil? ? false : true
end

helper_method :current_user, :logged_in?
end
